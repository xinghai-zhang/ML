# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:02:32 2015

@author: Xinghai
"""

import pandas as pd
import numpy as np

def haversine(coord1,coord2):
    import math
    sin = math.sin
    cos = math.cos
    atan2 = math.atan2
    sqrt = math.sqrt
    
    lon1,lat1=coord1
    lon2,lat2=coord2
    R=6371000 #metres
    phi1=lat1 * (3.1415 / 180)
    phi2=lat2 * (3.1415 / 180)
    Dphi= phi2 - phi1
    Dlambda = (lon2 -lon1) *  (3.1415 / 180)

    a = sin(Dphi / 2) ** 2 + cos(phi1)*cos(phi2) *sin(Dlambda/2)**2
    c = 2 * atan2(sqrt(a),sqrt(1-a))
    d = R*c
    return d
    

def speeds(polyline):
    N=len(polyline)
    v = [0.]*N
    if N == 0:
        return []
    
    for i in range(N - 1):
        v[i] = haversine(polyline[i],polyline[i+1]) / 15.
    
    v[N-1]  = haversine(polyline[N-1],polyline[N-2]) / 15.
    
    return v
    
def mean(df):
    return np.mean(df)

df = pd.read_csv('test.csv',sep=',', index_col=0)
df['LENGTH']=((df['POLYLINE'].str.count(',')+1) /2).round(decimals=0, out=None)
df.POLYLINE = df.POLYLINE.apply(eval)#from string to list of coords
df['SPEED'] = df.POLYLINE.apply(speeds)
df['AVERAGE']= df.SPEED.apply(mean)

df.to_csv('test_complete.csv')

