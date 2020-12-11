import json
with open('config.json') as json_file:
    data = json.load(json_file)
    api_key = data['covid']

    print(api_key)