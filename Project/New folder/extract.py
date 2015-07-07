# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:45:04 2015

@author: Xinghai
"""
" extract data that's within the testing timestamp"
import pandas as pd
import datetime

import csv

df = pd.read_csv('train.csv',sep=',', index_col=0)
#test = pd.read_csv('test.csv',sep=',',index_col=5)
df['DATETIME'] = pd.to_datetime(df['TIMESTAMP'], box = 'true', utc = 'true',unit='s')
df.index = df['DATETIME']

#test.index = pd.to_datetime(test.index, box = 'true', utc = 'true',unit='s')

#test0 = test.between_time(start_time='17:54:17', end_time='18:00:00')

#df0 = df.between_time(start_time='16:02:20', end_time='17:59:53')
#df1 = df.between_time(start_time='06:41:32', end_time='08:29:44 ')
#df2 = df.between_time(start_time='15:09:05', end_time='17:44:33')
#df3 = df.between_time(start_time='02:37:17', end_time='03:59:28')
#df4 = df.between_time(start_time='11:39:46', end_time='14:29:19')

#df0 = df.between_time(start_time='14:27:05', end_time='18:45:44')
#df1 = df.between_time(start_time='06:00:33', end_time='09:15:44')
#df2 = df.between_time(start_time='01:55:33', end_time='04:45:44')
df3 = df.between_time(start_time='10:55:33', end_time='15:15:44')

print("start")
#df0.to_csv('test0.csv')
#df1.to_csv('test1.csv')
#df2.to_csv('test2.csv')
#df3.to_csv('test3.csv')
#df4.to_csv('test4.csv')
#df0.to_csv('jun0.csv')
#df1.to_csv('jun1.csv')
#df2.to_csv('jun2.csv')
df3.to_csv('jun3.csv')
print("finish")

#test0.to_csv('test0.csv')

