import json

with open("config.json") as f:
    data = json.load(f)

for key in data["custom"]:
    prefix = key["prefix"]
    onMemberJoin = key["onMemberJoin"]
    onMemberRemove = key["onMemberRemove"]

for key in data["control"]:
    messageOnJoin = key["messageOnJoin"]
    messageOnRemove = key["messageOnRemove"]
    ping = key["ping"]
    _8Ball = key["_8Ball"]
    customStatus = key["customStatus"]