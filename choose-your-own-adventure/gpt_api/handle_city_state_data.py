""" """

import time
import random

import peewee
import requests
from typing import List, Tuple, Union, overload
from exc import NoMoreCitiesAvailable, FilterAvailableStates
from models.state_and_city import City, State, db

URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

@overload
def find_city_or_state(city_obj_list: List[Tuple[int, State]]) -> State: ...

@overload
def find_city_or_state(city_obj_list: List[Tuple[int, City]]) -> City: ...

def find_city_or_state(city_obj_list: Union[List[Tuple[int, City]],
                                            List[Tuple[int, State]]]
                                            ) -> Union[City, State]:
    """ Returns a city that has not yet been used. """
    while True:
        rand_int = random.randint(0, len(city_obj_list))
        city_filter = next(
            filter(lambda city: city[0] == rand_int, city_obj_list), None
        )
        if city_filter is None:
            raise FilterAvailableStates(
                "There is a really bad issue that is not fixable you are dying."
                "Probably when filtering cities."
            )
        _, city = city_filter
        return city

def generate_city_to_find() -> str:
    """ Generates a city to find now. """
    states = State.get_unused_states()
    state_mapping = [(i, c) for i, c in enumerate(states)]
    # Gets all of the states
    state = find_city_or_state(state_mapping)
    # Gets the cities in Washington
    city_db = City.get_unused_cities_by_state(state.name)
    wash_cities = [(i, c) for i, c in enumerate(city_db)]
    if not len(wash_cities):
        raise NoMoreCitiesAvailable("Used all available cities.")
    city = find_city_or_state(wash_cities)
    return f"{city.city_name}, {city.state.name}"

def upload_data(batch_start: int, batch_limit: int = 66570) -> int:
    """ TODO Total offsets = 66570 """
    states = State.get_all_states()
    state_names = {s.name for s in states}
    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }
    while batch_start <= batch_limit:
        # 10 limit is the max
        querystring = {"countryIds": "US", "offset": batch_start, "limit": 10}
        response = requests.get(URL, headers=headers, params=querystring)
        json_resp = response.json()
        try:
            for data in json_resp["data"]:
                region = data["region"]
                city = data["city"]
                cur_state = State(name=region)
                if region not in state_names:
                    state_names.add(region)
                    cur_state.save()
                else:
                    states = State.get_all_states()
                    cur_state = next((s for s in states if s.name == region), None)
                    if cur_state is None:
                        print("State: ", region, " not in state_names even after finding.")
                        print()
                        print("==State Names==")
                        print(state_names)
                        print()
                        print("State is not currently in the list of states")
                        time.sleep(2)
                        # raise ValueError("State problem")

                try:
                    City(city_name=city, state=cur_state).save()
                except peewee.IntegrityError as e:
                    print("Error:", e)
                    print("Error adding city", city, "for state", region)
                    print()
                # The offset is not in batches but by singular cities
                batch_start += 1
            time.sleep(1)
        except KeyError as k:
            print("Failed on a key error", k, "at i = ", batch_start)
            print("JSON Response:", json_resp)
            return batch_start
    return batch_start
