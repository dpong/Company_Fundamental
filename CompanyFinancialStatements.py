#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:49:03 2019

資料來源：https://financialmodelingprep.com

@author: dpong
"""

import json,requests,pickle,os
import datetime
import pandas as pd

time = datetime.datetime.now()
year = time.year
month = time.month

class Fundamental():
    def __init__(self,ticker):
        self.ticker = ticker

    def get_profile(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Company_profile_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/company/profile/'+'{}'.format(self.ticker)
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df['Keys'] = dataset['profile'].keys()
            df=df.set_index('Keys')
            df['profile'] = dataset['profile'].values()
            with open('Fundamental_data/{}_Company_profile_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(df,f)
        else:
            print('Already have {}_Company_profile'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Company_profile_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df = pickle.load(pickle_in)
        self.all_profile_data = df
        
    def get_quarterly_income(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Quarterly_income_statement_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/'+'{}'.format(self.ticker)+'?period=quarter'
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df['Keys'] = dataset['financials'][0].keys()
            df=df.set_index('Keys')
            dicts = len(dataset['financials'])
            for i in range(dicts):
                df['{}_Quarter'.format(i)] = dataset['financials'][i].values()
            with open('Fundamental_data/{}_Quarterly_income_statement_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(df,f)
        else:
            print('Already have {}_Quarterly_income_statement'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Quarterly_income_statement_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df = pickle.load(pickle_in)
        self.all_income_data = df

    def get_quarterly_balance_sheet(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Quarterly_balance_sheet_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/'+'{}'.format(self.ticker)+'?period=quarter'
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df['Keys'] = dataset['financials'][0].keys()
            df=df.set_index('Keys')
            dicts = len(dataset['financials'])
            for i in range(dicts):
                df['{}_Quarter'.format(i)] = dataset['financials'][i].values()
            with open('Fundamental_data/{}_Quarterly_balance_sheet_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(df,f)
        else:
            print('Already have {}_Quarterly_balance_sheet'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Quarterly_balance_sheet_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df = pickle.load(pickle_in)
        self.all_balance_sheet_data = df

    def get_quarterly_cash_flow(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Quarterly_cash_flow_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/'+'{}'.format(self.ticker)+'?period=quarter'
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df['Keys'] = dataset['financials'][0].keys()
            df=df.set_index('Keys')
            dicts = len(dataset['financials'])
            for i in range(dicts):
                df['{}_Quarter'.format(i)] = dataset['financials'][i].values()
            with open('Fundamental_data/{}_Quarterly_cash_flow_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(df,f)
        else:
            print('Already have {}_Quarterly_cash_flow'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Quarterly_cash_flow_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df = pickle.load(pickle_in)
        self.all_cash_flow_data = df

    def get_quarterly_financial_growth(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Quarterly_financial_growth_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/financial-statement-growth/'+'{}'.format(self.ticker)+'?period=quarter'
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df['Keys'] = dataset['growth'][0].keys()
            df=df.set_index('Keys')
            dicts = len(dataset['growth'])
            for i in range(dicts):
                df['{}_Quarter'.format(i)] = dataset['growth'][i].values()
            with open('Fundamental_data/{}_Quarterly_financial_growth_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(df,f)
        else:
            print('Already have {}_Quarterly_financial_growth'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Quarterly_financial_growth_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df = pickle.load(pickle_in)
        self.all_financial_growth_data = df

    def get_quarterly_key_metrics(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Quarterly_key_metrics_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/company-key-metrics/'+'{}'.format(self.ticker)
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df['Keys'] = dataset['metrics'][0].keys()
            df=df.set_index('Keys')
            dicts = len(dataset['metrics'])
            for i in range(dicts):
                df['{}_Quarter'.format(i)] = dataset['metrics'][i].values()
            with open('Fundamental_data/{}_Quarterly_key_metrics_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(df,f)
        else:
            print('Already have {}_Quarterly_key_metrics'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Quarterly_key_metrics_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df = pickle.load(pickle_in)
        self.all_key_metrics = df    

    def get_company_rating(self,year=year,month=month):
        if not os.path.exists('Fundamental_data'):
            os.makedirs('Fundamental_data')   
        if not os.path.exists('Fundamental_data/{}_Company_rating_{}_{}.pickle'.format(self.ticker,year,month)):
            url = 'https://financialmodelingprep.com/api/v3/company/rating/'+'{}'.format(self.ticker)
            response = requests.get(url)
            dataset = response.json()
            df = pd.DataFrame()
            df_detail = pd.DataFrame()
            df['Keys'] = dataset['rating'].keys()
            df=df.set_index('Keys')
            df['rating'] = dataset['rating'].values()
            df_detail['Keys'] = dataset['ratingDetails']['DCF'].keys()
            df_detail=df_detail.set_index('Keys')
            df_detail['DCF'] = dataset['ratingDetails']['DCF'].values()
            df_detail['ROE'] = dataset['ratingDetails']['ROE'].values()
            df_detail['ROA'] = dataset['ratingDetails']['ROA'].values()
            df_detail['D/E'] = dataset['ratingDetails']['D/E'].values()
            df_detail['P/E'] = dataset['ratingDetails']['P/E'].values()
            df_detail['P/B'] = dataset['ratingDetails']['P/B'].values()
            pickle_save = [df,df_detail]
            with open('Fundamental_data/{}_Company_rating_{}_{}.pickle'.format(self.ticker,year,month),'wb') as f:
                pickle.dump(pickle_save,f)
        else:
            print('Already have {}_Company_rating'.format(self.ticker))
            pickle_in = open('Fundamental_data/{}_Company_rating_{}_{}.pickle'.format(self.ticker,year,month),'rb')    
            df, df_detail = pickle.load(pickle_in)
        self.rating = df
        self.rating_detail = df_detail





