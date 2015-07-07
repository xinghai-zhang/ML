# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:16:59 2015

@author: Xinghai
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm

def main():
    df = pd.read_csv('new0.csv',sep=',', index_col=0)
    dummy_ranks = pd.get_dummies(df['CALL_TYPE'], prefix='CALL_TYPE')
#    df['L_LENGTH']= df['LENGTH']**2
#    df['L_AVERAGE']= df['AVERAGE']**2
    cols_to_keep = ['TOTAL', 'LENGTH', 'AVERAGE']#,'L_LENGTH','L_AVERAGE'
    data = df[cols_to_keep].join(dummy_ranks.ix[:, 'CALL_TYPE_':])
    train_cols = data.columns[1:]
    
    ols = sm.OLS(data['TOTAL'],data[train_cols])
    result = ols.fit()
    print(result.summary())
    
    df1 = pd.read_csv('test_complete.csv',sep=',', index_col=0)
# recreate the dummy variables
    combos = pd.DataFrame(df1, columns = ['CALL_TYPE', 'LENGTH', 'AVERAGE'])
    #combos.columns = ['CALL_TYPE', 'LENGTH', 'AVERAGE']
    dummy_ranks = pd.get_dummies(combos['CALL_TYPE'], prefix='CALL_TYPE')
    dummy_ranks.columns = ['CALL_TYPE_A', 'CALL_TYPE_B', 'CALL_TYPE_C']
 
# keep only what we need for making predictions
    cols_to_keep = ['LENGTH', 'AVERAGE']
    combos = combos[cols_to_keep].join(dummy_ranks.ix[:, 'CALL_TYPE_A':])
    
# make predictions on the enumerated dataset
    combos['pred'] = result.predict(combos[train_cols])
    combos['pred'] = combos['pred']*14
    combos.loc[combos['pred'] < 0] = 900
    combos['pred'].to_csv('submit0.csv')
main()