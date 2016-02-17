import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import itertools

# remember to set the index_col=False to avoid pandas using 1st col as indexes
df=pd.read_csv('../data/iepage.csv',index_col=False,sep=';')
#print df.head()
page_df=df['pages'].apply(lambda x: pd.Series(x.split('/')))
#print page_df.head()
page_list=list(page_df)
#print page_list
page_list.remove(0)
del page_list[5:19]
#print page_list

page_df2=page_df[page_list]
#print page_df2.head()

result=pd.concat([df,page_df2], axis=1)
ls_result=list(result)
ls_result.remove('pages')
result=result[ls_result]

d=df.to_dict()
print d.keys()



