""" AUTH: Models to authenticate the user's API access. """

from __future__ import annotations
from dataclasses import dataclass
import json
from typing import ClassVar

import os

@dataclass
class _ConfigLoader:
    """ _ConfigLoader class

    Private class to store API keys generated from a local file.

    Attributes:
        openai_key:
        geo_key:
        events_key:
    """
    openai_key: str
    geo_key: str
    events_key: str

class APIAuthentication:
    """ APIAuthentication class

        Class for authenticating APIs before querying for data.

    """
    _loaded_config: ClassVar[_ConfigLoader | None] = None

    def __init__(self, file_path: str) -> None:
        self.overall_path = os.getcwd().split("ChooseYourAdventure")[0] + file_path

    def get_openai_key(self) -> str:
        """ Returns the user's openai API key. """
        if self._loaded_config is None:
            self._loaded_config = self._generate_config()
        return self._loaded_config.openai_key

    def get_serp_api_key(self) -> str:
        """ Returns the user's serp API key. """
        if self._loaded_config is None:
            self._loaded_config = self._generate_config()
        return self._loaded_config.events_key

    def get_rapid_api_key(self) -> str:
        """ Returns the user's rapid API key. """
        if self._loaded_config is None:
            self._loaded_config = self._generate_config()
        return self._loaded_config.geo_key

    def _generate_config(self) -> _ConfigLoader:
        """ Generates the serp, openai, and rapid API keys and returns a
            _ConfigLoader object with the keys. """
        with open(self.overall_path, "r") as f:
            read_file = json.load(f)
        return _ConfigLoader(
            read_file["openai_api_key"],
            read_file["geo_api_key"],
            read_file["events_api_key"],
        )
