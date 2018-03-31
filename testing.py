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
act.positions={'QWARK': {'coins': 200000.0, 'notional': 2.028, 'original_direction': 'long', 'realized_pl': 0, 'vwap': 1.014e-05}, 'LTC': {'coins': 400.0, 'notional': 6.804, 'original_direction': 'long', 'realized_pl': 0, 'vwap': 0.01701}}
act.getPortfolio()

test_trade_dict={'notional_delta': 5.6895, 'cash_delta': -5.6895, 'position_delta': 100.0, 'ticker': 'ETH', 'original_tradetype': 'long'}

''' end testing the accounts class '''

''' test retrieve markets and calculate p/l '''
ticker_array=act.positions.keys()
retm=rm.RetrieveMarkets()
prices_dict=retm.getCurrentPrice(ticker_array)
