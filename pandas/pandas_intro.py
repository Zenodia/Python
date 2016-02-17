import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
# pandas series is a one-dimensional labeled array capable of holding any data type
#example:passing a list into pandas series
s=pd.Series([1,3,5,np.nan,6,8]) #one can see that passing in a list, index is created automatically
print s, s.index
#example: passing in a dict into pandas series
d = {'a' : 0., 'b' : 1., 'c' : 2., 'd':3., 'e':4.}
sd=pd.Series(d)
print sd

#get an element by indexes
print "get an element by indexes in s series, note the index is numerical", s.index, s[0]
print "get element by indexes in pd.Series(d) , note that the index is a-z",sd.index, sd['a']

#series can be operated like numpy array when doing addition. but different index scheme might result in na values
print s+sd

#moving to dataframe
#dataframe is 2-dimension labeled data structure with columns of different data types
#example1: use dict created by series to construct dataframe
d1 = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df1 = pd.DataFrame(d1)
print df1, type(df1)

#example2:create dataframe by pass a numpy array with datetime index
dates=pd.date_range('20160101', periods=10)
print dates
df0 = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list('ABCD'))
print df0

# example3:create dataframe by passing a dict obhect which look like series
df2=pd.DataFrame({'A' : 1.,
                  'B' : pd.Timestamp('20130102'),
                  'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D' : np.array([3] * 4,dtype='int32'),
                  'E' : pd.Categorical(["test","train","test","train"]),
                  'F' : 'foo' })
print df2
#example4: create dataframe by passing a list of dicts
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df3=pd.DataFrame(data2)
print df3

#example5: create df by passing dict of tuples
df4=pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
print df4
"""
print "display all columns' types of df", df2.dtypes
# viewing top or bottom of the dataframe
print "display first 5 in df",  df.head()
print "display last 3 of df", df.tail(3)

# display index, columns and numpy dta
print "display index of df", df.index
print "display columns of df",df.columns
print "display values of df", df.values

# describe the data similar to r summary function
print "describe the dataframe", df.describe()

#turn columns into row and rows into columns
print "transpose row and columns",df.T

#sort the data by an axis
print "sort rows by alphabet column names z-a", df.sort_index(axis=1, ascending=False)
print "sort rows by alphabet column names a-z", df.sort_index(axis=1, ascending=True)

# sort by a certain columns' names
print "sort rows by certain columns names", df.sort(['B','C'])


#subsetting dataframe --------------------
# selecting one column yields Series =df.A
print " type of a single column is Series",df['A'], df['A'].dtypes
print " same thing if we use this expression",df.A, df.A.dtypes

#subsetting by rows
print "selecting by first 3 rows ", df[0:3]

#subsetting by label
print "slicing by indexing rows=dates",df.loc[dates[0]]
print "slicing by 1st 3rows0selecting date range and then columns by names",df.loc['20160101':'20160103',['A','B']]

#select by position
#print df
print "selecting the 3rd row for all columns", df.iloc[3]
"""
