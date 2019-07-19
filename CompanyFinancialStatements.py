#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:49:03 2019

資料來源：https://financialmodelingprep.com

@author: dpong
"""

import json,requests,pickle,os
import pandas as pd


def get_profile(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Company_profile.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/company/profile/'+'{}'.format(ticker)
        response = requests.get(url)
        dataset = response.json()
        df = pd.DataFrame()
        df['Keys'] = dataset['profile'].keys()
        df=df.set_index('Keys')
        df['profile'] = dataset['profile'].values()
        with open('Fundamental_data/{}_Company_profile.pickle'.format(ticker),'wb') as f:
            pickle.dump(df,f)
    else:
        print('Already have {}_Company_profile'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Company_profile.pickle'.format(ticker),'rb')    
        df = pickle.load(pickle_in)
    return df

def get_quarterly_income(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Quarterly_income_statement.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/'+'{}'.format(ticker)+'?period=quarter'
        response = requests.get(url)
        dataset = response.json()
        df = pd.DataFrame()
        df['Keys'] = dataset['financials'][0].keys()
        df=df.set_index('Keys')
        dicts = len(dataset['financials'])
        for i in range(dicts):
            df['{}_Quarter'.format(i)] = dataset['financials'][i].values()
        with open('Fundamental_data/{}_Quarterly_income_statement.pickle'.format(ticker),'wb') as f:
            pickle.dump(df,f)
    else:
        print('Already have {}_Quarterly_income_statement'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Quarterly_income_statement.pickle'.format(ticker),'rb')    
        df = pickle.load(pickle_in)
    return df

def get_quarterly_balance_sheet(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Quarterly_balance_sheet.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/'+'{}'.format(ticker)+'?period=quarter'
        response = requests.get(url)
        dataset = response.json()
        df = pd.DataFrame()
        df['Keys'] = dataset['financials'][0].keys()
        df=df.set_index('Keys')
        dicts = len(dataset['financials'])
        for i in range(dicts):
            df['{}_Quarter'.format(i)] = dataset['financials'][i].values()
        with open('Fundamental_data/{}_Quarterly_balance_sheet.pickle'.format(ticker),'wb') as f:
            pickle.dump(df,f)
    else:
        print('Already have {}_Quarterly_balance_sheet'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Quarterly_balance_sheet.pickle'.format(ticker),'rb')    
        df = pickle.load(pickle_in)
    return df

def get_quarterly_cash_flow(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Quarterly_cash_flow.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/'+'{}'.format(ticker)+'?period=quarter'
        response = requests.get(url)
        dataset = response.json()
        df = pd.DataFrame()
        df['Keys'] = dataset['financials'][0].keys()
        df=df.set_index('Keys')
        dicts = len(dataset['financials'])
        for i in range(dicts):
            df['{}_Quarter'.format(i)] = dataset['financials'][i].values()
        with open('Fundamental_data/{}_Quarterly_cash_flow.pickle'.format(ticker),'wb') as f:
            pickle.dump(df,f)
    else:
        print('Already have {}_Quarterly_cash_flow'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Quarterly_cash_flow.pickle'.format(ticker),'rb')    
        df = pickle.load(pickle_in)
    return df

def get_quarterly_financial_growth(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Quarterly_financial_growth.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/financial-statement-growth/'+'{}'.format(ticker)+'?period=quarter'
        response = requests.get(url)
        dataset = response.json()
        df = pd.DataFrame()
        df['Keys'] = dataset['growth'][0].keys()
        df=df.set_index('Keys')
        dicts = len(dataset['growth'])
        for i in range(dicts):
            df['{}_Quarter'.format(i)] = dataset['growth'][i].values()
        with open('Fundamental_data/{}_Quarterly_financial_growth.pickle'.format(ticker),'wb') as f:
            pickle.dump(df,f)
    else:
        print('Already have {}_Quarterly_financial_growth'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Quarterly_financial_growth.pickle'.format(ticker),'rb')    
        df = pickle.load(pickle_in)
    return df

def get_quarterly_key_metrics(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Quarterly_key_metrics.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/company-key-metrics/'+'{}'.format(ticker)
        response = requests.get(url)
        dataset = response.json()
        df = pd.DataFrame()
        df['Keys'] = dataset['metrics'][0].keys()
        df=df.set_index('Keys')
        dicts = len(dataset['metrics'])
        for i in range(dicts):
            df['{}_Quarter'.format(i)] = dataset['metrics'][i].values()
        with open('Fundamental_data/{}_Quarterly_key_metrics.pickle'.format(ticker),'wb') as f:
            pickle.dump(df,f)
    else:
        print('Already have {}_Quarterly_key_metrics'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Quarterly_key_metrics.pickle'.format(ticker),'rb')    
        df = pickle.load(pickle_in)
    return df

def get_company_rating(ticker):
    if not os.path.exists('Fundamental_data'):
        os.makedirs('Fundamental_data')   
    if not os.path.exists('Fundamental_data/{}_Company_rating.pickle'.format(ticker)):
        url = 'https://financialmodelingprep.com/api/v3/company/rating/'+'{}'.format(ticker)
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
        with open('Fundamental_data/{}_Company_rating.pickle'.format(ticker),'wb') as f:
            pickle.dump(pickle_save,f)
    else:
        print('Already have {}_Company_rating'.format(ticker))
        pickle_in = open('Fundamental_data/{}_Company_rating.pickle'.format(ticker),'rb')    
        df, df_detail = pickle.load(pickle_in)
    return df,df_detail


