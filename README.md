# ChooseYourAdventure

A GPT backed engine to generate a trip and highlight events in the US. 

You'll need:
An openai API key
An Rapid API api key 
And a serp API api key to generate all content

These apis should be stored in a file in  ```cwd/configs/adventure_config.json```.

`{"openai_api_key": "OPENAI_API_KEY", "geo_api_key": "RAPID_API_KEY", "events_api_key": "SERP_API_KEY"}`


To run the program:
After cloning first `cd` into the `choose-your-own-adventure ` directory and start the Flask serverand run start the local react development server by running this code:
```
cd choose-your-own-adventure
yarn start-api
yarn start
```

Have fun seeing the US!
