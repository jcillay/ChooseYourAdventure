""" FLASK: Server for providing destination, GPT generated itinerary for ]
    destination, and events in the specified location """
from __future__ import annotations
from typing import Any

from flask import Flask
import openai
from serpapi import GoogleSearch

import exc
from gpt_trip_data import get_trip, Trip
from handle_city_state_data import generate_city_to_find
from models.event import Event
import api_auth

app = Flask(__name__)

app.config["FLASK_APP"] = "server"
app.config["FLASK_ENV"] = "development"

@app.route("/location")
def generate_gpt_response() -> dict[str, Any]:
    """ Returns a response of a location, city, and state. Each item is a string,
        where the location is a string formatted as `city, state`. """
    i = 0
    while i < 10:
        try:
            location = generate_city_to_find()
            city, state = location.split(",")
            return {"location": location, "city": city, "state": state}
        except exc.FilterAvailableStates:
            i += 1
        if i == 10:
            raise exc.NoMoreCitiesAvailable("Tried to find a city too many times")
    return {"ERROR": "NO CITY FOUND"}

@app.route("/gpt-data/<string:city>/<string:state>")
def get_gpt_data(city: str, state: str) -> dict[str, Trip]:
    """ Generates a trip itinerary using gpt-3.5-turbo and returns """
    authentication = api_auth.APIAuthentication("configs/adventure_config.json")
    openai.api_key = authentication.get_openai_key()
    location = city + "," + state

    query_str = f"Create a trip itinerary for a {location}, with a " \
                "total days, itinerary_by_day which should a list containing a " \
                "morning, afternoon, and evening list of activities for each day. " \
                "Return them in JSON like this: "
    json_format = """ {
        "total_days": …,
        "itinerary_by_day: [
            "one": {
                "morning": [
                    ..., ..., ...
                ],
                "afternoon": [
                    ..., ..., ...
                ],
                "evening":[
                    ..., ..., ...
                ]
            },
            {
                "morning": [
                    ..., ..., ...
                ],
                "afternoon": [
                    ..., ..., ...
                ],
                "evening": [
                    ..., ..., ...
                ]
            },
        ],
    }

    All character values should be Strings, with the exception of "dps" which should be a Double. """
    # content_query = f"How many days should I spend in {location}? Give me " \
    #                 "an itinerary by day, with a morning, evening and afternoon " \
    #                 "schedule that is easily parsable. Do not include a Note at the end. "\
    #                 "Please the text 'Duration:' followed by the total time of the trip."
    content_query = query_str + json_format
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a trip itinerary planner."},
            {"role": "user", "content": content_query},
        ],
    )
    message = response.choices[0]['message']  # type: ignore Need to specify the return of the response
    print("{}: {}".format(message['role'], message['content']))
    trip = get_trip(message["content"])
    return {"gpt_data": trip}

@app.route("/google-events/<string:city>/<string:state>/")
def get_events_in_state(city: str, state: str) -> dict[str, Any]:
    """ Gets Google Event data for a city and state. """
    authentication = api_auth.APIAuthentication("configs/adventure_config.json")
    serp_api_key = authentication.get_serp_api_key()
    params = {
      "engine": "google_events",
      "q": f"Events in {city}, {state}",
      "hl": "en",
      "gl": "us",
      "api_key": serp_api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    event_results = results.get("events_results", None)
    if event_results is None:
        print("No Results")
        return {"status": "error", "events": []}

    events = []
    for e in event_results:
        kwargs = {}
        if "title" in e:
            kwargs["title"] = e["title"]
        if "link" in e:
            kwargs["link"] = e["link"]
        if "description" in e:
            kwargs["description"] = e["description"]
        if "venue" in e and "name" in e["venue"]:
            kwargs["where"] = e["venue"]["name"]
        if "date" in e and "when" in e["date"]:
            kwargs["time"] = e["date"]["when"]
        events.append(Event(**kwargs))
    return {"status": "success", "events": events}
