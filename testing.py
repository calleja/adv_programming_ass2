#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:03:30 2018

@author: lechuza
"""

import sys
import imp
sys.path.append('/home/lechuza/Documents/CUNY/data_607/assignment2/gitCode')
sys.path.append('/home/tio/Documents/CUNY/advancedProgramming/ass2/adv_programming_ass2')
import retrieveMarkets as rm
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import engageUser as eu
import ass1_acountsClass as accts
import mongoDB_interface as mongo
import requests
imp.reload(eu)

retm=rm.RetrieveMarkets()
retm.getCurrentPrice('ETH')
test=retm.getCurrencies()
df=retm.df_active
type(df.loc[35,'Currency'])

diag=eu.Dialogue()
diag.engageUser()
#TODO check the trade log to ensure that all the trade data looks appropriate, then build the interace with the db

#test the p&l calculations... create a portfolio of accounts

''' testing the accounts class '''
act=accts.Account()
act.positions={'QWARK': {'coins': 200000.0, 'notional': 2.028, 'original_direction': 'long', 'realized_pl': 0, 'vwap': 1.014e-05}, 'LTC': {'coins': 40000.0, 'notional': 6.804, 'original_direction': 'long', 'realized_pl': 0, 'vwap': 0.01701}}
act.getPortfolio()

test_trade_dict={'notional_delta': 5.6895, 'cash_delta': -5.6895, 'position_delta': 100.0, 'ticker': 'ETH', 'original_tradetype': 'long'}

cash={'cash':{'coins':0,'notional':0,'original_direction':'','realized_pl':0,'vwap':0,'total p/l':None,'proportion_shares':None,'proportion_notional':None}}
test_df=pd.DataFrame.from_dict(cash,orient='index')
test_df.columns
df.columns
pd.concat([df,test_df],axis=1)

''' end testing the accounts class '''

''' convert the portfolio dictionary into a pd.DataFrame '''
df=pd.DataFrame.from_dict(act.positions,orient='index')
df['proportion_shares']=df.apply(lambda x: x['coins']/sum(df['coins']),axis=1)
df['proportion_notional']=df.apply(lambda x: x['notional']/sum(df['notional']),axis=1)
dic={'original_direction':'','realized_pl':'','vwap':0,'total p/l':None,'proportion_shares':None,'proportion_notional':None}


''' test retrieve markets and calculate p/l '''
datetime.datetime.now() - datetime.timedelta(days=100)

ticker_array=act.positions.keys()
retm=rm.RetrieveMarkets()
prices_dict=retm.getCurrentPrice(ticker_array)
''' end retrieve markets '''

''' test retrieve markets and the 24 hour price executions '''

url_24_hr='https://min-api.cryptocompare.com/data/histohour?'
        
api_key='c8f16ead26d4438e991c318c8fd76629'
api_secret='bb885473805547f1834cfc5057a78901'        
market='BTC'+'-'+'ETH'
payload2={'apikey':api_key,
'apisecret':api_secret,'nonce':datetime.datetime.now(),'market':market,'limit':24}

payload2={'apikey':api_key,
'apisecret':api_secret,'nonce':datetime.datetime.now(),'fsym':'BTC','tsym':'ETH','limit':24}


r=requests.get(url_24_hr,params=payload2) 
r.json().keys()
r.json()['Data'][5].keys()
df=pd.DataFrame.from_dict(r.json()['Data'])
['high']            
mat=df['high'].as_matrix()
df.columns
df_mat=df.as_matrix()
np.amax(df_mat[:,1])
np.amin(df_mat[:,1])
np.average(df_mat[:,1])
np.std(mat)

get24Hr(['ETH'])

def get24Hr(ticker_list):
    url_24_hr='https://min-api.cryptocompare.com/data/histohour?'
    stats_dic={}
    api_key='c8f16ead26d4438e991c318c8fd76629'
    api_secret='bb885473805547f1834cfc5057a78901'        
    for single_tick in ticker_list:
            #look up the ticker from the index number
            #instantiate the dicitonary
        stats_dic[single_tick]={}
        payload2={'apikey':api_key,
'apisecret':api_secret,'nonce':datetime.datetime.now(),'fsym':single_tick,'tsym':'BTC','limit':24}
        r=requests.get(url_24_hr,params=payload2) 
        df=pd.DataFrame.from_dict(r.json()['Data'])
        df_mat=df.as_matrix()
        stats_dic[single_tick]['max']=np.amax(df_mat[:,1])
        stats_dic[single_tick]['min']=np.amin(df_mat[:,1])
        stats_dic[single_tick]['avg']=np.average(df_mat[:,1])
    return(stats_dic)

''' end testing retrieveMarkets '''            

''' test the mongo injection '''
trade1={'side':'long',
'ticker':'OMG',
'quantity':38566,
'executed price':0.026733,
'execution timesestamp':datetime.datetime.now(),
'money in/out':233.543,
'original_tradetype':'long',
'position_delta':299000,
'new_cash_bal':778999}


trade2={'side':'long',
'ticker':'RPL',
'quantity':34566,
'executed price':.006733,
'execution timesestamp':datetime.datetime.now(),
'money in/out':23.543,
'original_tradetype':'long',
'position_delta':20000,
'new_cash_bal':678999}

trade3={'side':'sell to close',
'ticker':'KWK',
'quantity':40000,
'executed price':.000453,
'execution timesestamp':datetime.datetime.now(),
'money in/out':120.1433,
'original_tradetype':'long',
'position_delta':-40000,
'new_cash_bal':453768}

m=mongo.MongoInterface()
m.clearCollection()
m.tradeInjection(trade1)
m.tradeInjection(trade2)
m.tradeInjection(trade3)
df=m.retrieveTrades()
m.retrieveAll()

