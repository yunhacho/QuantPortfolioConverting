import os
import sys
import locale
import pandas as pd
import numpy as np
from _datetime import datetime, timezone
path="C:/Users/user/Documents/DART/QuantPortforlioConverting/RData/data"
os.chdir(path)

locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
data_market=pd.read_csv('data_market.csv', engine='python')
data_market=data_market.drop(data_market.columns[0], axis='columns')

#gilmes(): 데이터 구조 확인하기
#glimse(data_market)

#head(names(data_market),10)

# 열 이름 바꾸기
lst=list(data_market.columns)
lst[lst.index('시가총액.원.')]='시가총액'
data_market.columns=lst

#unique(): 고유한 값 확인
print(pd.unique(data_market['SEC_NM_KOR']).tolist())

#loc() : 원하는 열 선택
print(data_market.loc[:, '종목명'].head(5))
print(data_market.loc[:, ['종목명', 'PBR', 'SEC_NM_KOR']].head(5))
ser=pd.Series(data_market.columns)
print(data_market.loc[:, ser[ser.str.startswith('시', na=False)]].head(5))
print(data_market.loc[:, ser[ser.str.endswith('R', na=False)]].head(5))
print(data_market.loc[:, ser[ser.str.contains('가', na=False)]].head(5))

# 열 생성 및 데이터 변형
data_market['PBR']=pd.to_numeric(data_market['PBR'], errors='coerce')
data_market['PER']=pd.to_numeric(data_market['PER'], errors='coerce')

data_market._set_value(data_market['PBR']=='-','PBR', np.nan)
data_market._set_value(data_market['PER']=='-','PBR', np.nan)

data_market['ROE']=data_market.apply(lambda x : x['PBR']/x['PER']
                                     if((x['PBR']!='NaN')and(x['PER']!='NaN'))
                                     else np.nan, axis=1)
data_market['ROE']=data_market.apply(lambda x : round(x['ROE'],4)
                                     if(x['ROE']!='NaN')
                                     else np.nan, axis=1)
data_market['size']= data_market.apply(lambda x: 'big'
                                       if (x['시가총액']>=np.nanmedian(data_market['시가총액']))
                                       else 'small', axis=1)

print(data_market.loc[:, ['종목명', 'ROE', 'size']].head(5))

#조건을 충족하는 행 선택
print(data_market[data_market.PBR < 1][['종목명','PBR']].head(5))

print(data_market[(data_market.PBR < 1) & (data_market.PER <20)
                  & (data_market.ROE > 0.1)][['종목명', 'PBR', 'PER', 'ROE']].head(5))

#요약 통계값 계산 summerize
#data_market.describe()
print(data_market[data_market.시장구분 =='코스피'][['PBR']].max(skipna=True))
print(data_market[data_market.시장구분 =='코스피'][['PBR']].min(skipna=True))

#sort_values() : 데이터 정렬
print(data_market.PBR.sort_values().head(5))
print(data_market[data_market.시장구분 =='코스피']
      [['종목명','ROE']].sort_values(by='ROE', ascending=False).head(5))

#g순위 계산
data_market['PBR_rank']=data_market[data_market.시장구분 =='코스피'][['PBR']]\
    .rank(method='first', ascending=True)
print(data_market[data_market.시장구분 =='코스피'][['종목명', 'PBR', 'PBR_rank']]
      .sort_values(by='PBR', ascending=True).head(10))  #by='PBR_rank' 로 하면 rank 순 맞춰서 더 잘나옴

#분위 수 계산
data_market['PBR_tile']=pd.qcut(data_market.PBR, 5, labels=np.arange(1,6))
print(data_market.loc[:, ['종목명', 'PBR', 'PBR_tile']].sort_values(by='PBR').head(10))

#그룹별로 데이터 묶기
data_market['SEC_NM_KOR']=data_market['SEC_NM_KOR'].astype(str) # Nan column 보이게끔
print(data_market.groupby(by=['SEC_NM_KOR']).count())
#print(data_market.groupby(by=['SEC_NM_KOR'])['종목코드'].count())
#print(pd.unique(data_market['SEC_NM_KOR']).tolist())

print(data_market.groupby(['시장구분', 'SEC_NM_KOR']).PBR.median().sort_values())



