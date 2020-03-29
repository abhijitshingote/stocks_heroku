import os

import psycopg2
import re
import requests
import pandas as pd
import datetime
import yfinance as yf
import sqlalchemy
from io import StringIO


DATABASE_URL = os.environ['DATABASE_URL']
engine = sqlalchemy.create_engine(DATABASE_URL,connect_args={'sslmode':'require'})


with open('stocklist.txt') as fread:
	uniquesymbolsonly=fread.read()
uniquesymbolsonly=uniquesymbolsonly.split('||')
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

Get_Data_From_Yahoo_full_load(uniquesymbolsonly)	


for filename in ['populate_stockinfotable_from_local_insert.sql','cleanup_stockinfotable.sql','removeduplicates_from_stockpricehistory.sql','other_scripts.sql']:

	file = open('sql_files/'+filename)
	escaped_sql = sqlalchemy.text(file.read())
	# print(escaped_sql)
	engine.execute(escaped_sql.execution_options(autocommit=True))
	print('First Load - Successful -',filename)

