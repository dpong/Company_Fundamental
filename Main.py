#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:49:19 2019

@author: dpong
"""

import CompanyFinancialStatements
import pickle,os
import pandas as pd


ticker_list = ['CBL','CYH','DISH','FTR','GNW','HOV','HTZ',
               'LXK','MBI','MNK','NM','RCII','STX','TACN','XRX']

total = pd.DataFrame(columns=ticker_list)
total['Keys'] = ['score', 'recommendation', 'rating']
total = total.set_index('Keys')


for ticker in ticker_list:
    try:
        df,df_detail=CompanyFinancialStatements.get_company_rating('{}'.format(ticker))
        total['{}'.format(ticker)] = df['rating']
    except:
        pass
    

  

