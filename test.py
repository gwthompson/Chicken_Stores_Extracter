import json
from pprint import pprint

with open('stores.json', 'r') as r:
    for line in r:
        l = json.loads(line)

print(len(l['body']['items']))
