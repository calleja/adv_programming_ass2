#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:47:44 2018

@author: lechuza
"""

import pymongo
import pandas as pd
import numpy as np
import datetime
from time import sleep

#exposed port on the docker mongo container: 27017
#sudo docker run -it -p 81:27017 mongo
client=pymongo.MongoClient('mongodb://tio:persyy@ds131329.mlab.com:31329/crypto_trades')
db=client.crypto_trades
trades=db.trade_collection

trade_list=[]
for i in range(5):
    trade_list.append({'notional_delta': 5.6895, 'cash_delta': -5.6895, 'position_delta': 100.0, 'ticker': 'ETH', 'original_tradetype': 'long','tradetime':datetime.datetime.now()})
    sleep(2)
    
for i in trade_list:    
    trades.insert_one(i)



#will return all documents in a collection
g=trades.find()

for i in g:
    print(i)
    
#place all documents into a pandas dataframe
df=pd.DataFrame(list(g))    
