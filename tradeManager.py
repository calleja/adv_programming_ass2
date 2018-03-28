#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class interacts with the tradeClass and stores a log of all the trades. This facilitates p+l calculation and the trade log.

Blotter requirements:
    side (Buy/Sell), Ticker
    Qty, Executed Price
    Timestamp, Money In/Out
    
P/L:
    Ticker, current position (can be 0),
    Current Market Price, VWAP,
    Unrealized p/l, realized p/l
"""
import sys
import pandas as pd
sys.path.append('/usr/src/app/PROJECT_FOLDER')
sys.path.append('/home/lechuza/Documents/CUNY/data_607/assignment1/ass1_fromWork')
sys.path.append('/home/tio/Documents/CUNY/advancedProgramming/ass1_fromWork')
import tradeClass as trade

class TradingDay(object):
    
    def __init__(self):
        self.tradeLogTup=()
        
    def makeTrade(self,rawTradeDict,act):
        #TODO validate the trade, attach a "post-trade cash balance" element and record in the mongoDB db      
        specificTrade=trade.EquityTrade(rawTradeDict,act)
        #an instantiation of EquityTrade class... no processing done yet
        
        #TODO ensure that illegal trades are not logged... this logic is contained within tradeClass.qaTrade() function
        try:
            specificTradeResult=specificTrade.tradeType()
            #TODO must append cash position to the trade dict... can either do here or in tradeClass... tradeClass is preferred
            formattedDic=self.prepDict(specificTradeResult,rawTradeDict)
            self.logTrade(formattedDic)
            print('your trade has been logged')
            return(specificTradeResult)
        except ValueError:
            #TODO ensure this breaks out of the function
            print('trade was not executed')
            raise ValueError #pass the ValueError to the calling function in engageUser class
        #a dictionary of scrubbed and processed trade attributes... unfortunately, this does not handle an errant trade
        #TODO ensure that illegal trades are not logged... this logic is contained within tradeClass.qaTrade() function... this function does not and should not handle errant trades... need to ensure that the application breaks and that prepDic() is not called
        
        
    def prepDict(self,tradeClassDict,rawDict):        
        #take elements from both dictionaries and create a third one for logging... this will need to formatted before displaying to users
        formattedDict={'side':rawDict['tradetype'],'ticker':rawDict['ticker'],'quantity':rawDict['shares'],'executed price':rawDict['price'],'execution timesestamp':rawDict['timestamp'],'money in/out':tradeClassDict['cash_delta'],'original_tradetype':tradeClassDict['original_tradetype'],'position_delta':tradeClassDict['position_delta']}
        return(formattedDict)
        
    def logTrade(self,tradeObject):
        #TODO store all the trade records into a mongo db collection; each entry is first encapsulated into a dictionary. Requirements: timestamp, money in/out (in appropriate units), cash balance - AFTER the trade is execute - of the account (in base currency), qty, ticker and direction (buy/sell)
        self.tradeLogTup=(tradeObject,)+self.tradeLogTup
        #create another function to format the trade list, unless this method is light
        return
    def profitCalc(self):
        #handle the p+l
        return
    
    def prettyPrintTradeLog(self):
        return print(pd.DataFrame(list(self.tradeLogTup)))
    
    def sortTrades(self):
        #place tickers of trades in a pandas df of ticker and timestamp; groupBy ticker and select for the latest timestamp, then sort by timestamp
        df=pd.DataFrame(list(self.tradeLogTup))

        g=df.groupby('ticker').apply(lambda x: x['execution timesestamp'].max())

        g.sort_values(ascending=False,inplace=True)
        traded_ticks=g.index.tolist()
        universe=['AMZN','AAPL','SNAP','INTC','MSFT']
        [traded_ticks.append(x) for x in universe if x not in traded_ticks]
        return(list(traded_ticks))
    
        
