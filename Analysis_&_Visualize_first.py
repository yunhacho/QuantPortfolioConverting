import os
import sys
import locale
import pandas as pd
from _datetime import datetime, timezone
path="C:/Users/user/Documents/DART/QuantPortforlioConverting/RData/data"
os.chdir(path)

locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
KOR_ticker = pd.read_csv("KOR_ticker.csv",engine='python')
KOR_sector = pd.read_csv("KOR_sector.csv", engine='python')
KOR_ticker = KOR_ticker.drop(KOR_ticker.columns[0], axis='columns')
KOR_sector = KOR_sector.drop(KOR_sector.columns[0], axis='columns')


KOR_ticker['종목코드']=KOR_ticker['종목코드'].astype('str')
KOR_sector['CMP_CD']=KOR_sector['CMP_CD'].astype('str')
code_series=pd.Series(KOR_ticker['종목코드'])
KOR_ticker['종목코드']=code_series.str.pad(width=6,side='left',fillchar='0')
code_series=pd.Series(KOR_sector['CMP_CD'])
KOR_sector['CMP_CD']=code_series.str.pad(width=6, side='left', fillchar='0')

KOR_sector=KOR_sector.drop(['CMP_KOR'], axis='columns')
lst=list(KOR_sector.columns)
lst[lst.index('CMP_CD')]= '종목코드'
KOR_sector.columns=lst
#print(KOR_sector)
data_market = pd.merge(KOR_ticker, KOR_sector, on='종목코드',how='left')
data_market.to_csv('data_market_py.csv', na_rep='NA', encoding='utf-8')
print(data_market)
