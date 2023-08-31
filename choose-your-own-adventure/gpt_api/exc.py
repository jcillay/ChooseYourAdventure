
class GPTBaseError(Exception):
    """ """
    def __init__(self, msg, *args: object) -> None:
        super().__init__(*args)
        self.msg = msg

class FilterAvailableStates(GPTBaseError):
    """ """

class NoMoreCitiesAvailable(GPTBaseError):
    """ """

class NoMoreStatesAvailable(GPTBaseError):
    """ """
