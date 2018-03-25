#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:03:30 2018

@author: lechuza
"""

import sys
import imp
sys.path.append('/home/lechuza/Documents/CUNY/data_607/assignment2/gitCode')
import retrieveMarkets as rm
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import engageUser as eu
imp.reload(eu)

retm=rm.RetrieveMarkets()
test=retm.getCurrencies()
df=retm.df_active
type(df.loc[35,'Currency'])

diag=eu.Dialogue()
diag.engageUser()


h=datetime.datetime.now() - datetime.timedelta(days=120)

type(h)

df=pd.DataFrame.from_dict(d)

r=df['close'].rolling(window=20).mean()
df['ma_20']=r
df.dtypes
df['time'].head()

df['time']=df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))



plt.subplot(1,1,1)
plt.xticks(rotation=45)
plt.plot(df['time'],df['close'],color='red',marker='o')
plt.plot(df['time'],df['close'],color='green',linestyle='-')
plt.plot(df['time'],df['ma_20'],color='cyan',linestyle='-')
#plt.title(str(self.market)+' pair')
plt.show()
plt.close()