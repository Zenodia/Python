import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import itertools

# remember to set the index_col=False to avoid pandas using 1st col as indexes
df=pd.read_csv('../data/NOemailclicks.csv',index_col=False,sep=';')

# get list of column headers=dates and skipping the cookieID column
hls=list(df)


#convert dataframe df to dictionary with visitorcookieId as key
df_dict=df.set_index("VisitorCookieID").T.to_dict()

#sorted(df_dict[612288343].items())
#print df_dict[612288343], type(df_dict[612288343])

# convert all date corresponding values to 1

def only_1s(d2):
    to_ones={}
    for k2,v2 in d2.iteritems():
        if v2>=1:
            to_ones[k2]=1
        else:
            to_ones[k2]=0
    sorted(to_ones, key=lambda key:to_ones[key])
    return to_ones

def nested_dict(d1):
    new_d={}
    for k1,v1 in d1.iteritems():
        new_d[k1]=only_1s(v1)
    
    return new_d

new_dict=nested_dict(df_dict)

print new_dict[612288343]

#convert back to dataframe
backtodf=pd.DataFrame(new_dict).T

print backtodf.head()


#backtodf.to_csv('../outputfile/NOpivot1s.csv')

# keep the last click per cookie
def keep_first(df1):
    dfls=list(df1)
    l=len(dfls)
    rowindex=df1.index.values
    rowcount=len(rowindex)
    for i in range(0,rowcount):
        #reversed for loop looking from last column to first column
        for j in range(l,0,-1):
            if df1.iloc[i][dfls[j-1]]==1:
                df1.loc[rowindex[i],dfls[j-2]]==0
            else:
                continue
    return df1


    
