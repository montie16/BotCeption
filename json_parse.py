import json
from pprint import pprint

with open('botception_TwitterFeed.json') as data_files:
    data = json.load(data_files)
pprint(data)