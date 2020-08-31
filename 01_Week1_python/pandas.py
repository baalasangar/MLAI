# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 14:54:52 2020

@author: 118183
"""

import numpy as np
import pandas as pd
# How to create Series from Numpy

np_array = np.random.randn(10)
pd.Series(np_array)
# Custome way to define the index for the serioue
pd.Series(np_array, index=np.arange(1, 11, dtype=int))

# Creating serious from dict
data = {'a' : 0., 'b' : 1., 'c' : 2.}
# Key will be the index for the Serious
pd.Series(data)

#  Accessing the data from serious
s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
s
s['d']  # return 4 - accessing by Index key
s[3]  # retuens 4 - accessing by the location 
s[:3] # returns all the values from location 0 -2
s[:] # retuen all the values in the serious
s[-3:] # '-' specifies to calculate from reverse
s[['a','b']]

# Creating Dataframe

df2 = pd.DataFrame(np.random.randn(5,5))

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'], 'Age':[28,34,29,42]}
pd.DataFrame(data, index=[0,1,2,3])

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data,index=["first","second"])
df['d'] = pd.Series([20,30],index=["first","second"])

df['a']  # retuen the values of "a" column
df.loc["first"]  # return the value of "first" row
df.iloc[1]  # retriving the rows by index


df1 = pd.DataFrame(np.random.randn(4, 6))
df1[1]

