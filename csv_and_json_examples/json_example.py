import requests
import json


if __name__ == '__main__':
    r = requests.get('https://danepubliczne.imgw.pl/api/data/synop')

    print(json.loads(r.text)[0])
    # print(r.json()[0])
