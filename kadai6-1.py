# 千葉県の宿泊旅行統計
# e-Stat APIを使って、2016年の千葉県に住む人の海外出張に関する旅行統計（平均泊数など）を取得します。
#statsDataIdで調査を指定し、cdCatやcdAreaなどで絞り込みます。


import requests
import json

APP_ID = "9dfc580965226dac8fdd4bb3f40e461546ab4272"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003300761",
    "cdCat01": "130",    
    "cdCat02": "100",
    "cdCat03": "110",     
    "cdArea": "00120",   
    "time": "2016000000",
    "metaGetFlg": "Y",
    "lang": "J"
}

response = requests.get(API_URL, params=params)
data = response.json()
print(json.dumps(data, indent=2, ensure_ascii=False))
