import json
from urllib.request import urlopen


def GetVanillappHandler(url):
    data = urlopen(f'https://vanillapp.ir/api/check/?target={url}').read()
    parseToJson = json.loads(data)
    response = { 'IsSuccess': parseToJson['status'] }
    return response