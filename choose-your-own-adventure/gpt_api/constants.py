""" Static variables to import into server files. """

JSON_QUERY_FORMAT = """ {
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


