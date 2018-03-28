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

#calculate and add the cash balance after trade. The prospective classes to do so:
#trade transaction dictionary is complete... we log the trade by a function in the tradeManager class: logTrade()

''' testing the accounts class '''
act=accts.Account()

test_trade_dict={'notional_delta': 5.6895, 'cash_delta': -5.6895, 'position_delta': 100.0, 'ticker': 'ETH', 'original_tradetype': 'long'}

act.postEquityTrade(test_trade_dict)

''' end testing the accounts class '''