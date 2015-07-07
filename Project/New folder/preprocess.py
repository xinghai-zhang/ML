# -*- coding: utf-8 -*-

import numpy as np
from sklearn import mixture
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import sys
import pandas as pd
import csv


def countPts(master):
    df = pd.DataFrame(master, columns = ['POLYLINE'])
    master['LENGTH'] = ((df['POLYLINE'].str.count(',')+1) /2).round(decimals=0, out=None)


def main():
    df0 = pd.read_csv('df0.csv',sep=',', index_col=0)
    df1 = pd.read_csv('df1.csv',sep=',', index_col=0)
    df2 = pd.read_csv('df2.csv',sep=',', index_col=0)
    df3 = pd.read_csv('df3.csv',sep=',', index_col=0)
    df4 = pd.read_csv('df4.csv',sep=',', index_col=0)
    
    countPts(df0)
    countPts(df1)
    countPts(df2)
    countPts(df3)
    countPts(df4)
    
    df0.to_csv('test0.csv')
    df1.to_csv('test1.csv')
    df2.to_csv('test2.csv')
    df3.to_csv('test3.csv')
    df4.to_csv('test4.csv')

   
#df['LENGTH'] =

main()
#print(df1)    print(master)