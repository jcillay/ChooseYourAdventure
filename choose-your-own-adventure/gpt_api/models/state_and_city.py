""" MODEL: State and City models. """
from typing import List, Optional

import peewee
import typing_extensions

db = peewee.SqliteDatabase("state-cities.db")

class State(peewee.Model):
    """ State class

    PeeWee DB object to store a state in the US

    Class Attributes:L
        name: Character Field of size 30 that stores the name of the US state.
            NOTE: This values must be unique so no name is stored twice
        all_cities_selected: True if all cities in the State have already been
            queried for, False otherwise """
    name = peewee.CharField(30, unique=True)
    all_cities_selected = peewee.BooleanField(default=False)

    class Meta:
        database = db

    @classmethod
    def get_unused_states(cls) -> List[typing_extensions.Self]:
        """ Selects State objects where not all of the cities have been queried
            for.

            Returns: List of State objects. """
        return cls.select().where(cls.all_cities_selected == False).execute()

    @classmethod
    def get_all_states(cls) -> List[typing_extensions.Self]:
        """ Returns a list of States currently in the DB. """
        return cls.select().execute()

    @classmethod
    def get_state_by_name(cls, name: str) -> Optional[typing_extensions.Self]:
        """ Selects a single state object by name from the DB.

            Args:
                name: State name to query for

            Returns: A single state from the given name, or None if a name with
                that state is not in the DB. """
        return cls.select().where(cls.name == name).execute()


class City(peewee.Model):
    """ City class

    DB object to store us City information

    Class Attributes:
        city_name: Name of the city
        state: State object to look up in the DB
        used_before: True if the City has been queried for, False otherwise

    """
    city_name = peewee.TextField(False)
    state = peewee.ForeignKeyField(State, backref="cities")
    used_before = peewee.BooleanField(default=False)

    class Meta:
        database = db
        indexes = (
            (('city_name', 'state'), True),
        )

    @classmethod
    def get_unused_cities_by_state(cls, state_name: str) -> List[typing_extensions.Self]:
        """ Returns a list of City objects by the State's name.

            Args:
                state_name: State's name as a string

            Returns: List of City objects """
        return cls.select().where(State.name == state_name and cls.used_before == False).execute()

    @classmethod
    def get_all_city_names(cls) -> List[str]:
        """ Returns a list of City's city_name currently in the DB. """
        return [c.city_name for c in cls.select().execute()]
