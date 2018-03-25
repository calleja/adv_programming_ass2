#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Will need to retrieve universe of available currencies from bittrex and place into a pd df
"""
import pandas as pd
import requests
import datetime
import hmac
import hashlib
import time #to convert UNIX timestamp
import matplotlib.pyplot as plt
import numpy as np

class RetrieveMarkets():
    #some global variables for Bittrex
    
    def __init__(self):
        self.api_key='c8f16ead26d4438e991c318c8fd76629'
        self.api_secret='bb885473805547f1834cfc5057a78901'
        self.base_currency='BTC'        

    def getCurrencies(self):
        
        url='https://bittrex.com/api/v1.1/public/getcurrencies'
        #all arguments must be converted to string
        payload={'apikey':self.api_key,
'apisecret':self.api_secret,'nonce':datetime.datetime.now()}

        r=requests.get(url,params=payload)
        df=pd.DataFrame(r.json()['result'])
        self.df_active=df[df.IsActive == True]
    #display this dataframe to the user
        return(self.df_active.loc[:,['Currency','CurrencyLong']])


    def getCurrentPrice(self,ticker):
        url_current='https://bittrex.com/api/v1.1/public/getticker'
#must be a BTC based cross market
        self.market=self.base_currency+'-'+ticker
        payload2={'apikey':self.api_key,
'apisecret':self.api_secret,'nonce':datetime.datetime.now(),'market':self.market}
        r=requests.get(url_current,params=payload2)
        #returns the ask, bid, last trades in a dict container
        what=r.json()['result']
        return(what)
        
        
    def get100Day(self,ticker_index):
        ''' Acquire historical prices from CRYPTOCOMPARE '''
        url='https://min-api.cryptocompare.com/data/histoday'
        #will return a str
        ticker=self.df_active.loc[ticker_index,'Currency']
#prices from last 120 days
        parameters= {'fsym':ticker, 'tsym': self.base_currency, 'e': 'Bittrex', 'aggregate':1,'limit':120}
        
        r=requests.get(url,parameters)
        #handle this error in the calling class
        j_obj=r.json()
        if j_obj['Response']=='Error':
            print("fetch didn't work")
            raise RuntimeError
        raw_time=j_obj['Data']
        df=pd.DataFrame.from_dict(raw_time)
        df['time']=df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))
        self.draw100day(df,ticker)
    
    
    def draw100day(self,df,ticker):
        df['ma_20']=df['close'].rolling(20).mean()
        
        plt.subplot(1,1,1)
        plt.xticks(rotation=45)
        #plt.plot(df['time'],df['close'],color='red',marker='o')
        plt.plot(df['time'],df['close'],color='green',linestyle='-')
        plt.plot(df['time'],df['ma_20'],color='cyan',linestyle='-')
#plt.title(str(self.market)+' pair') 
        plt.title('100 day and 20 day MA: '+str(self.base_currency)+'-'+ticker+' pair')
        plt.show()
        plt.close()
        return()