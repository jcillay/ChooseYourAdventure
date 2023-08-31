from typing import Dict, List
import openai
import requests
import peewee
import mysql.connector
from models.state_and_city import db, State, City
import handle_city_state_data
# db.create_tables([State, City])
# handle_city_state_data.upload_data(300)
for s in City.get_all_city_names():
    print(s)

# state_city_mapping: Dict[str, List[str]] = {}
# with open("states.txt", "r+") as f:
#     states = list(map(lambda s: s.replace("\n", ""), f.readlines()))

# with open("washington_cities.txt", "r+") as f:
#     cities = list(map(lambda s: s.replace("\n", ""), f.readlines()))

# db.connect()
# db.drop_tables([State, City])
# db.create_tables([State, City])

# # Insert all of the data and do stuff to it
# State.insert_many([(s,) for s in states], fields=[State.name]).execute()
# wazzu = State.select().where(State.name == "Washington")

# City.insert_many([(c, wazzu) for c in cities], fields=[City.city_name, City.state]).execute()


# city_db = City.select().where(City.state == wazzu)
# print("FIRST CITY DB")
# for c in city_db:
#     assert type(c) == City
#     print(c.city_name)
# print("Update")
# nrows = (City
#          .update(city_name="BLAH")
#          .where(City.state==wazzu)
#          .execute())
# sec_db = City.select().where(City.state == wazzu)
# print(nrows)
# print()
# print("Second CITY DB")
# print()
# for c in sec_db:
#     assert type(c) == City
#     print(c.city_name)


# for s in State.select():
#     print(s.name)



# SECRET API KEY DONT LOSE IT
# openai.api_key = ""



# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {"role": "system", "content": "You are a trip itinerary planner."},
#         {"role": "user", "content": "How many days should I spend in New York, NewYork? Give me an itinerary."},
#     ],

#     )

# print(response)
# print(response.__dict__)
# message = response.choices[0]['message']
# print("{}: {}".format(message['role'], message['content']))
# import requests

# url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q65/locatedIn"

# headers = {
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response)
# print(response.__dict__)

# with open("~/Desktop/practice/ChooseYourAdventure/choose-your-own-adventure/gpt_api/states.txt", "r+") as f:

state_city_mapping: Dict[str, List[str]] = {}
with open("states.txt", "r+") as f:
    states = list(map(lambda s: s.replace("\n", ""), f.readlines()))

with open("washington_cities.txt", "r+") as f:
    cities = list(map(lambda s: s.replace("\n", ""), f.readlines()))

state_city_mapping["Washington"] = cities

# import requests

# # url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
# url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions?offset=01&limit=10"

# # querystring = {"countryIds":"US"}

# headers = {
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers) #, params=querystring)

# print(response.json())

# GETS US COUNTRY
# import requests

# {'data': [{'code': 'US', 'currencyCodes': ['USD'],
#            'name': 'United States of America', 'wikiDataId': 'Q30'}],
#            'metadata': {'currentOffset': 0, 'totalCount': 1}}


# url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries"

# querystring = {"namePrefix":"United States"}

# headers = {
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())

