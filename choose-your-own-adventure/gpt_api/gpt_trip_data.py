""" """
# PUBLIC_API = "sh428739766321522266746152871799"

import json
from typing import Dict, List

from dataclasses import dataclass, field

# with open("choose-your-own-adventure/gpt_api/example_gpt_response.txt", "r+") as f:
make_mapping: Dict[str, List[str]] = {}

@dataclass
class Day:
    """ Day class

    Contains information of activities for the user to do in a single day of
    their Trip.

    Attributes:
        morning_activities: Morning activities to do in a single day
        afternoon_activities: Afternoon activities to do in a single day
        evening_activities: Evening activities to do in a single day
    """
    morning_activities: List[str] = field(default_factory=list)
    afternoon_activities: List[str] = field(default_factory=list)
    evening_activities: List[str] = field(default_factory=list)

@dataclass
class Trip:
    """ Trip class

    Class Attributes:
        total_time: Time to spend in the generated location
        days: List of Days containing activities to do for each day
    """
    total_time: str
    days: List[Day] = field(default_factory=list)

def get_trip(gpt_string: str) -> Trip:
    """ Handles the GPT generated json interpreted as a string.

        Args:
            gpt_string: json formatted string for the identified location

        Returns: Trip object containing data for the itinerary """
    j_data = json.loads(gpt_string)
    days = [Day(d["morning"], d["afternoon"], d["evening"]) for d in j_data["itinerary_by_day"]]
    return Trip(total_time=j_data["total_days"], days=days)
