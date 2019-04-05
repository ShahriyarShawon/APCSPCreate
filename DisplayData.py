import json
# TODO: make sure the user has something to see

with open("database.json", "r+") as f:
    content = json.load(f)
    for thing in content["1"]:
        print(thing)