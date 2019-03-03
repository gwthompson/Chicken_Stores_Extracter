import requests
import os
import json
from pprint import pprint

## Loading API TOKEN given from the public database
with open(r'credential.json', 'r') as r:
    j = json.load(r)
    API_TOKEN = j['API_TOKEN']

BASE = 'http://apis.data.go.kr/B553077/api/open/sdsc/'
category = 'largeUpjongList'

def upJong(divId, key, numOfRows=100, pageNo=1, type='json'):
    operation = 'storeListInUpjong'
    op_BASE = BASE + operation
    options = {'ServiceKey': API_TOKEN,
               'type': type,
               'divId': divId,
               'key': key,
               'numOfRows': numOfRows,
               'pageNo': pageNo}
    ops_str = "&".join("%s=%s" % (k,v) for k,v in options.items())
    r = requests.get(op_BASE, params=ops_str)
    return r.json()

p = 1
l = upJong('indsSclsCd', 'Q05A08', numOfRows=100, pageNo=p)
print(l['header'])
while True:
    p += 1
    ll = upJong('indsSclsCd', 'Q05A08', numOfRows=100, pageNo=p)
    if ll['header']['resultCode'] == '03':
        break
    l['body']['items'].extend(ll['body']['items'])

with open('stores.json', 'w') as r:
    json.dump(l, r)