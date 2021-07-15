
from binance.client import Client
import os
import time
import numpy as np
import pandas as pd
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("SECRET_KEY")


client = Client(api_key, api_secret)
		# client from B.
simbolo='ATOMUSDT'
'''
while True:
# get market depth  (Booklet)
	depth = client.get_order_book(symbol=simbolo, limit = 10) # 'ATOMUSDT'

#lista = list(depth.items())
#to get value: d[key]
#ask_list = lista[1]
#bid_list = lista[2]
	bid_list = depth['bids'] #BUY green
	ask_list = depth['asks'] #SELL red
# ['Price', 'Amount']

#print("\t\t\t\t\t|" +simbolo+ "|")
#print("\tAsks: \t-Green-\t\t|\tBids: \t-Red-")
#for n in range(0, len(bid_list)):
	n = 0
	
	# ---------- BID ---------
	bidPrice = float(bid_list[n][0]) # 0.0000 | 0.00
	bidAmount = float(bid_list[n][1])
	# ---------- ASK ---------
	askPrice = float(ask_list[n][0]) # 0.0000 | 0.00
	askAmount = float(ask_list[n][1])
	# ------- printing -------
	
	print("\t[%.4f] (" % bidPrice + 
		 "%.2f) \t" % bidAmount +
		 "\t[%.4f] (" % askPrice +
		 "%.2f)" % askAmount)
	time.sleep(2)
#klines = client.get_historical_klines(simbolo, Client.KLINE_INTERVAL_1MINUTE, "1 hour ago UTC")
'''
print(client.get_asset_balance("USDT"))

margin_d=client.get_margin_account()
m_assets = margin_d["userAssets"]
portafoliom = []
portafoliom_assets = []
portafoliom_free =[]
portafoliom_borrowed = []
portafoliom_locked = []
for i in range(len(m_assets)):
	if (float(m_assets[i]['free']) or
	float(m_assets[i]['borrowed']) or
	float(m_assets[i]['locked'])) != 0:
		portafoliom.append(m_assets[i])
		portafoliom_assets.append(
			m_assets[i]["asset"])

for i in range(len(portafoliom_assets)):
	portafoliom_free.append(
		portafoliom[i]["free"])
	portafoliom_borrowed.append(
		portafoliom[i]["borrowed"])
	portafoliom_locked.append(
		portafoliom[i]["locked"])

#for i in range(len(portafoliom)):
margin_array_iso = np.array([#portafoliom_assets,
					portafoliom_free,
					portafoliom_borrowed,
					portafoliom_locked])
print("\tMargin (Cross), portafolio:")
print(portafoliom_assets)
print(margin_array_iso)
print(pd.DataFrame(margin_array_iso,
		columns= portafoliom_assets)
		)

	
#print(client.get_margin_account( symbol="BUSD"))
dit = {}
#dict
