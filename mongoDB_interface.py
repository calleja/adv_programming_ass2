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

class MongoInterface(object):
    def __init__(self):
        self.checkConnection()

    def checkConnection(self):
        try:
            client=pymongo.MongoClient('mongodb://tio:persyy@ds131329.mlab.com:31329/crypto_trades',serverSelectionTimeoutMS=3000)
            client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            #try to connect one more time
            print('trying to connect one more time')
            client=pymongo.MongoClient('mongodb://tio:persyy@ds131329.mlab.com:31329/crypto_trades',serverSelectionTimeoutMS=7000)
        self.db=client.crypto_trades
        self.trades=self.db.trade_collection
        
    def tradeInjection(self,doc):
        self.trades.insert_one(doc)
        return
    
    def retrieveTrades(self):
        rs=self.trades.find().sort({'execution timestamp':-1})
        #works in robo3t: db.trade_collection.find().sort({'execution timestamp':-1})
        return(pd.DataFrame(list(rs)))
    
    def clearCollection(self):
        self.trades.remove()
        return
    
    def retrieveAll(self):
        rs=self.trades.find()
        return(pd.DataFrame(list(rs)))
'''
        trade_list=[]
for i in range(5):
    trade_list.append({'notional_delta': 5.6895, 'cash_delta': -5.6895, 'position_delta': 100.0, 'ticker': 'ETH', 'original_tradetype': 'long','tradetime':datetime.datetime.now()})
    sleep(2)
    
for i in trade_list:    
    trades.insert_one(i)
'''

