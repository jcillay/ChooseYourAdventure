# ChooseYourAdventure

A GPT backed engine to generate a trip and highlight events in the US. 

You'll need:
An openai API key
An Rapid API api key 
And a serp API api key to generate all content

These apis should be stored in a file in  ```cwd/configs/adventure_config.json```.

`{"openai_api_key": "OPENAI_API_KEY", "geo_api_key": "RAPID_API_KEY", "events_api_key": "SERP_API_KEY"}`


To run the program:
After cloning first `cd` into the `choose-your-own-adventure ` directory and activate the venv. 

```
cd choose-your-own-adventure
source gpt_api/venv/bin/activate
```
Next install all python requirements using:

```
pip install -r gpt_api/requirements.txt
```
Finally, start the Flask server and the React development server:
```
yarn start-api
yarn start
```

Have fun seeing the US!
