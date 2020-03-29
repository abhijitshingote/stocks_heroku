import requests
from io import StringIO
import pandas as pd
import re


def GetStockList(url):
	r = requests.get(url)
	s=str(r.content,'utf-8')
	data = StringIO(s) 
	df=pd.read_csv(data)
	df=df[~df.Sector.isna()]
	return df['Symbol'].tolist()

req=requests.get(
'https://pkgstore.datahub.io/core/s-and-p-500-companies/constituents_json/data/64dd3e9582b936b0352fdd826ecd3c95/constituents_json.json')
sp500json=req.json()
sp500symbols=[]
for each in sp500json:
	sp500symbols.append(each['Symbol'])

# url_nasdaq='''https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'''
# url_amex='''https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download'''
# url_nyse='''https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download'''
url_all='''https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&render=download'''

# uniquesymbolsonly=list(set(GetStockList(url_nasdaq)+GetStockList(url_nyse)+GetStockList(url_amex)+sp500symbols))
uniquesymbolsonly=list(set(GetStockList(url_all) + sp500symbols))
uniquesymbolsonly= [sym for sym in uniquesymbolsonly if re.match("^[a-zA-Z]*$", sym)]

for sym in sp500symbols:
	try:
		uniquesymbolsonly.remove(sym)
		uniquesymbolsonly.insert(0,sym)
	except:
		continue

with open('stocklist.txt','w') as f:
	f.write('||'.join(uniquesymbolsonly))


