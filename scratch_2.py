from binance.client import Client
from os import environ as env
import numpy as np
import pandas as pd
from binance.client import Client

#archivo = open("Text.txt", "r")
lista = np.array(["Primera línea", "Segunda línea", "Tercera línea"])

tbnbkey = env.get("API_KEY")
tbnbsec = env.get("API_SECRET")
print(lista)

import requests
token_api_taapi = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZhYmlhbmtwa0BnbWFpbC5jb20iLCJpYXQiOjE2MTc0Nzk3MDQsImV4cCI6NzkyNDY3OTcwNH0.uWIyH_zRb_Gk3MgMq5CtYrh8gcUBG_TgdHx7R0FBoeo"

indicators = ['rsi', 'kdj', 'stochrsi']
timelines = ['1m', '3m', '5m', '15m', '30m',
             '1h', '2h', '4h', '6h', '12h',
             '1d', '3d', '1w']
portafolio = None  # extract from wallet's assets.
# ATTENTION! taapi and binance haven't same names pairs.
# TODO use .replace("/", "") for Binanace API.
params = {"secret": token_api_taapi, "exchange": "binance", "symbol": "ATOM/USDT", "interval": "1m"}
response = requests.get("https://api.taapi.io/rsi", params)
response2 = requests.get("https://api.taapi.io/kdj", params)
response3 = requests.get("https://api.taapi.io/stochrsi", params)
print(response.content)    # RSI
print(response2.content)   # KDJ
print(response3.content)  #StochRSI
py_json = response.json()
print(response2.json())
print(py_json)
print(py_json["value"])

client = Client(tbnbkey, tbnbsec)
print(client.get_asset_balance("USDT"))
# print(klines)
print(client.get_isolated_margin_account())
portafoliom_iso= client.\
    get_isolated_margin_account()["assets"] # gives a raw assets-list !
#portafoliom_iso_insider =
pair_list = []
for i in range(len(portafoliom_iso)):
    pair_list.append(portafoliom_iso[i]["symbol"])  # ATOMUSDT  (gives a str)
                                    # ADAETH
pairs = {}  # "Pair" : 'assets' & info.
for i in range(len(pair_list)):
    base_asset_asset = portafoliom_iso[i]["baseAsset"]["asset"]
    qote_asset_asset = portafoliom_iso[i]["quoteAsset"]["asset"]
    # keys = values →"ADAETH" : ["ADA","ETH"]
                            #  [bassea,quotea]
    pairs[pair_list[i]] = [base_asset_asset,
                           qote_asset_asset] # yet

#lista_akeys = client.get_isolated_margin_account().keys()
#lista_avalues=client.get_isolated_margin_account().values()

array = np.array([pair_list, pairs.values()])
arrayp= pd.DataFrame(array)
print(arrayp)
