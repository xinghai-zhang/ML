# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:10:13 2015

@author: Xinghai
"""

import pandas as pd
import numpy as np

def getLast(v):
    N = len(v)
    if N == 0:
        return 0
    return v[N-1]

df = pd.read_csv('new0.csv',sep=',', index_col=0)
df['speeds']=df.speeds.apply(eval)
df['last'] = df['speeds'].apply(getLast)
df.to_csv('new0.csv')
