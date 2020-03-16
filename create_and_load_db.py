import os
import psycopg2

import requests
import pandas as pd
import datetime
import yfinance as yf
import sqlalchemy
# import requests  
from io import StringIO


DATABASE_URL = os.environ['DATABASE_URL']
engine = sqlalchemy.create_engine(DATABASE_URL,connect_args={'sslmode':'require'})
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# cur = conn.cursor()
# cur.execute(""" create table public.price_history
# (
# symbol varchar(10),
# date_traded date,
# open_price float,
# high_price float,
# low_price float,
# close_price float,
# volume bigint
# ); """)


# def GetStockList(url):
# 	r = requests.get(url)
# 	s=str(r.content,'utf-8')
# 	data = StringIO(s) 
# 	return pd.read_csv(data)['Symbol'].tolist()

req=requests.get(
'https://pkgstore.datahub.io/core/s-and-p-500-companies/constituents_json/data/64dd3e9582b936b0352fdd826ecd3c95/constituents_json.json')
sp500json=req.json()
sp500symbols=[]
for each in sp500json:
	sp500symbols.append(each['Symbol'])
uniquesymbolsonly=sp500symbols
print('Got Stock Symbol Lists......Total Symbols - ',str(len(uniquesymbolsonly)))


def Get_Data_From_Yahoo_full_load(stocklist,period='1y'):

	print("Running FULL LOAD ")
	if not isinstance(stocklist,(list,tuple)):
		stocklist=[stocklist]
	
	stockinfo={}
	stockpricehistory=pd.DataFrame()
	
	for i in range(0,len(stocklist),100):

		print('Getting Chunk..'+str((i/100)+1)+' of '+str(len(stocklist)/100),flush=True)
		symbol_list_chunk=stocklist[i:i+100]
		# when the last chunk only contains one element, the returned df is in a different format
		# below if block is ensure returned df remains in same format
		if len(symbol_list_chunk) == 1:
			symbol_list_chunk.append("AAPL")
		stocklist_str=" ".join(symbol_list_chunk)
		print(stocklist_str)
		df=yf.download(stocklist_str,period='1y')
		indiv_df=pd.DataFrame()
		main_big_df=pd.DataFrame()
		downloadedsymbols=list(set([col[1] for col in df.columns]))
		for idx,symbol in enumerate(downloadedsymbols):
			print(symbol + '...'+str(idx+i+1)+' of '+str(len(stocklist)),flush=True)
			for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
				indiv_df[col]=df[col][symbol]
			indiv_df['symbol']=symbol
			main_big_df=main_big_df.append(indiv_df)
		main_big_df.to_sql('stock_price_history',engine,schema='public',if_exists='append')

Get_Data_From_Yahoo_full_load(uniquesymbolsonly[:4])	


for filename in ['populate_stockinfotable_from_local_insert.sql','cleanup_stockinfotable.sql','removeduplicates_from_stockpricehistory.sql','other_scripts.sql']:

	file = open('sql_files/'+filename)
	escaped_sql = sqlalchemy.text(file.read())
	# print(escaped_sql)
	engine.execute(escaped_sql.execution_options(autocommit=True))
	print('Issue -',filename)
# conn.commit()
# cur.close()
# conn.close()
