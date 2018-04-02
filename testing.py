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
import matplotlib.pyplot as plt
import engageUser as eu
import ass1_acountsClass as accts
import mongoDB_interface as mongo
imp.reload(mongo)

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
ticker_array=act.positions.keys()
retm=rm.RetrieveMarkets()
prices_dict=retm.getCurrentPrice(ticker_array)
''' end retrieve markets '''

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

