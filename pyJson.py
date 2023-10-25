import json

jsonString = '{ "name":"John", "age":30, "city":"New York"}'
dict = json.loads(jsonString)
print(dict["name"])
print(json.dumps(jsonString))
