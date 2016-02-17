import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
df=pd.read_csv("./data/testpanda.csv",sep=";",parse_dates=True,decimal=".",header=0) # read csv into data frame
#get header as a list for operation
collist=list(df)
#print collist

#get a list of out travel group sizes using column names
passlist=["OUT_NO_OF_INFANT","OUT_NO_OF_ADULT","OUT_NO_OF_STUDENT","OUT_NO_OF_SENIOR","OUT_NO_OF_CHILD"]
#print df[passlist]
# get a list of out group with kids in bookings
passwkids=["OUT_NO_OF_INFANT","OUT_NO_OF_CHILD"]

# get specific columns to sum up the passengers for out trip
df["OUT_gpSize"]=df[passlist].sum(axis=1)
df["OUT_Kids"]=df[passwkids].sum(axis=1)
#print df["OUT_gpSize"]
#print df["OUT_gpSize"].dtypes
#print df["OUT_Kids"]

#create category out of travel group sizes, taking in both total # ppl in the group and if they have kids
def cat_ppl(datf,gpsize,kids):
    cat=[]
    for row in datf[kids]:
        print "row; ", row
        for r in datf[gpsize]:
            print "r: " ,r
            if row!=np.nan:        
                if r <=0:
                    print "err:negative group size"
                elif r ==1:
                    cat.append("single no kids")
                elif r==2:
                    cat.append("couple no kids")
                elif r<=5:
                    cat.append("group 3-5,no kids")
                elif r<=10:
                    cat.append("group 6-10,no kids")
                elif r<=20:
                    cat.append("group of 11-20, no kids")
                elif r<=50:
                    cat.append("group of 30-50, no kids")
                elif r<=100:
                    cat.append("group of 51-100, no kids")
                else :
                    cat.append("large group >100, no kids")
            else:
                if r <=1:
                    print "err:impossible  group size:1 child"
                elif r==2:
                    cat.append("1 adult+1 kid")
                elif r==3:
                    cat.append("group of 3 with kid/kids")
                elif r<=6:
                    cat.append("group 4/5/6 travel with kid/kids")
                elif r<=10:
                    cat.append("group of 7-10 travel with kid/kids")
                elif r<=20:
                    cat.append("group of 11-20 travel with kid/kids")
                else :
                    cat.append("group more than 20 travel with kid/kids")        
    return cat
df["PassTravelgp_OUT"]=cat_ppl(df,"OUT_gpSize","OUT_Kids")
print df["PassTravelgp_OUT"]
