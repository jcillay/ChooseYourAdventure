""" Model: Event for each location"""

from dataclasses import dataclass

@dataclass
class Event:
    """ Event class

    Stores an upcoming event for a certain city and state

    Class Attributes:
        title: Title of the Event
        time: Time the event begins
        description: Description of the event
        where: Venue or place of the Event
        link: Link to the website of the Event (if available)
    """
    title: str = "No Title"
    time: str = "No Time Listed"
    description: str = "No Description"
    where: str = "No Location Given"
    link: str = "No Link To Event"
