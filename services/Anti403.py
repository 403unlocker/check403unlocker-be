import json
from urllib.request import urlopen

def GetAnti403Handler(url):
    data = urlopen(f'https://api.anti403.ir/api/search-filter?url={url}').read()
    parseToJson = json.loads(data)
    print(parseToJson)
    return parseToJson