import json
# with open("authenticate.json","r") as f:
#     j_content = json.load(f)
#     print(j_content["username"])


#changing json
with open("authenticate.json","a+") as f:
    content = json.load(f)
    content["first_time"] = "dingus"