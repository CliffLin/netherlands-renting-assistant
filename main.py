import json
import requests

from funda import Funda
from parariusScraper import Pararius

AREA = "amsterdam"
PRICE = [2000, 3000]
DATA = 'data.json'
HEADERS = {}

def loaddata():
    with open(DATA) as f:
        try:
            return json.load(f)
        except:
            return dict()

def savedata(data):
    with open(DATA, "w+") as f:
        f.write(json.dumps(data))


def process(localdata, houses, callback):
    for house in houses:
        if not localdata.get(str(house.id)):
            localdata[str(house.id)] = True
        else:
            continue

        try:
            callback(house)
        finally:
            savedata(localdata)

def sendToTelegram(house):
    CHATID = ''
    TOKEN = ''
    URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

    body = {'parse_mode': 'Markdown', 'chat_id': CHATID, 'text': '**%s**\n€%s/%s\n%s' % (house.address, house.price, house.living_area, house.URL)}
    requests.post(URL, json=body)

if __name__ == '__main__':
    svcs = [Funda, Pararius]
    for idx, svc in enumerate(svcs):
        svcs[idx] = svc(AREA, PRICE, header=HEADERS)

    data = loaddata()
    for svc in svcs:
        process(data, svc.Run(), sendToTelegram) 
