import json
with open("authenticate.json","r") as f:
    j_content = json.load(f)
    print(j_content["username"])