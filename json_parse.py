import re

shakes = open("BotCeption_TwitterFeed.json", "r")

for line in shakes:
    if re.match("where", line):
        print line