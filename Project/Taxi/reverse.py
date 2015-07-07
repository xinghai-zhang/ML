# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:38:42 2015

@author: Xinghai
"""

import pandas as pd
import numpy as np
import calendar
import datetime
from datetime import datetime as dt

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
    
def speeds(df):
    polyline = df['POLYLINE']
    N=df['past']
    v = [0.]*N
    if N == 0:
        return []
        
    for i in range(N - 1):
        v[i] = haversine(polyline[i],polyline[i+1]) / 15.
    v[N-1]  = haversine(polyline[N-1],polyline[N-2]) / 15.
    
    return v
    
def mean(df):
    return np.mean(df)
    



df = pd.read_csv('df0v1.csv',sep=',', index_col=0)

time = 18*3600 #18:00:00
#time = 8*3600+1800 #18:00:00
#time =17*3600+2700
#time = 4*3600
#time =14*3600+1800
df['diff'] =np.ma.masked
for i in range(len(df['LENGTH'])):
    date = dt.strptime(df.ix[i,8], "%Y-%m-%d %H:%M:%S")
    df.ix[i,10] = df.ix[i,9] - (calendar.timegm(dt.timetuple(datetime.datetime(date.year, date.month, date.day)))+time-df.ix[i,4])/15   
df = df.loc[df['diff'] >= 0]
df['past']=(df['LENGTH']-df['diff']).astype(int)
df.POLYLINE = df.POLYLINE.apply(eval)#from string to list of coords 
df['speeds'] = df.apply(speeds,axis = 1)
df['AVERAGE']= df.speeds.apply(mean)

df['TOTAL']=df['LENGTH']
df['LENGTH']=df['past']
cols_to_keep = ['TOTAL','CALL_TYPE' ,'LENGTH', 'AVERAGE']
df = df[cols_to_keep]

df.to_csv('new0.csv')



#print(df['DATETIME'])