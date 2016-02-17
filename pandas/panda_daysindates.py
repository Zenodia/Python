import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


# make a function to substract two dates and calculate days inbetween
# col1, col2 is in the format of "column_header" 
def daysin2dates(dataframe,col1,col2):
    daysbetween=[]
    for index ,row in df.iterrows(): # interate through rows inside dataframe
        #print  row["HOME_DEPARTURE_DATE"], row["OUT_DEPARTURE_DATE"]
        if row[col1]==np.nan:
            continue
        else:
            temp=(pd.to_datetime(row[col1])-pd.to_datetime(row[col2]))
        #print temp
        daysbetween.append(temp) # otherwise feed TravelDuration the returndate-1stdptdate
    return daysbetween


#sample application
df=pd.read_csv("./data/testpanda.csv",sep=";",parse_dates=True,decimal=".",header=0) # read csv into data frame
#convert column date and returndate into date&time format
pd.to_datetime(df["OUT_DEPARTURE_DATE"])
pd.to_datetime(df["HOME_DEPARTURE_DATE"])
pd.to_datetime(df["DATE_CREATED"])
pd.to_datetime(df["PAYMENT_DATE"])
#call the daysin2dates function like this 
travelduration=daysin2dates(df,"HOME_DEPARTURE_DATE","OUT_DEPARTURE_DATE")
df["TravelDuration"]=travelduration
print df["TravelDuration"]
