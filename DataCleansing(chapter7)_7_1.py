import os
import sys
import locale
import pandas as pd
from _datetime import datetime, timezone
path="C:/Users/user/Documents/DART/QuantPortforlioConverting/RData/data"
os.chdir(path)
#print(os.getcwd())
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
#print(locale.getlocale()) engine='python'

KOR_ticker = pd.read_csv("KOR_ticker.csv",engine='python')
KOR_ticker = KOR_ticker.drop(KOR_ticker.columns[0], axis='columns')
#print(KOR_ticker)
#KOR_ticker = pd.read_csv("KOR_ticker.csv",engine='python')
#print(KOR_ticker)
KOR_ticker['종목코드']=KOR_ticker['종목코드'].astype('str')
code_series=pd.Series(KOR_ticker['종목코드']) #시리즈형
KOR_ticker['종목코드']=code_series.str.pad(width=6,side='left',fillchar='0') #KOR_ticker['종목코드']는 문자열형
#print(KOR_ticker)

price_list=[]
os.chdir("C:/Users/user/Documents/DART/QuantPortforlioConverting/KOR_price")
#datetime=datetime.replace(tzinfo=timezone)
for i in range(1,KOR_ticker.shape[0]):
    name=KOR_ticker['종목코드'] [i]+'_price.csv'
    if(os.path.isfile(name)==False):
        print("No "+name)
        continue
    df=pd.read_csv(name, engine='python')
    df[df.columns[0]]=pd.to_datetime(df[df.columns[0]], format="%Y-%m-%d")
    #df.fillna(0)
    df.fillna(method='ffill') #왜 결측치 처리가 안되지..?
    #df.fillna(method='bfill')
    sr = pd.Series(list(df['Price']), name=KOR_ticker['종목코드'][i],index=df[df.columns[0]])
    price_list.append(sr)

df=pd.concat(price_list,axis=1)
print(df)

df.tail(n=5)



