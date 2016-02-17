import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
df=pd.read_csv("./data/testpanda.csv",sep=";",parse_dates=True,decimal=".",header=0) # read csv into data frame

#create category out of existing data, example, categorize revenue=totalprice
def cat_float(datf,c1):
    cat=[]
    for row in datf[c1]:
        if row <0:
            cat.append("minus")
        elif row==0:
            cat.append("zero")
        elif row <100:
            cat.append("<99")
        elif row <150:
            cat.append("<150")
        elif row <200:
            cat.append("<200")
        elif row <250:
            cat.append("<250")
        elif row <300:
            cat.append("<300")
        elif row <350:
            cat.append("<350")
        elif row <400:
            cat.append("<400")
        elif row <450:
            cat.append("<450")
        elif row <500:
            cat.append("<500")
        elif row <550:
            cat.append("<550")
        elif row <600:
            cat.append("<600")
        elif row <650:
            cat.append("<650")
        elif row <700:
            cat.append("<700")
        elif row <750:
            cat.append("<750")
        elif row <800:
            cat.append("<800")
        elif row <850:
            cat.append("<850")
        elif row <900:
            cat.append("<900")
        elif row <950:
            cat.append("<950")
        elif row <1000:
            cat.append("<1000")
        elif row <1500:
            cat.append("<1500")
        elif row <2000:
            cat.append("<2000")
        elif row <2500:
            cat.append("<2500")
        elif row <3000:
            cat.append("<3000")
        elif row <3500:
            cat.append("<3500")
        elif row <4000:
            cat.append("<4000")
        elif row <4500:
            cat.append("<4500")
        elif row <5000:
            cat.append("<5000")
        elif row <5500:
            cat.append("<5500")
        elif row <6000:
            cat.append("<6000")
        elif row <6500:
            cat.append("<6500")
        elif row <7000:
            cat.append("<7000")
        elif row <7500:
            cat.append("<7500")
        elif row <8000:
            cat.append("<8000")
        elif row <8500:
            cat.append("<8500")
        elif row <9000:
            cat.append("<9500")
        else:
            cat.append(">10000")
    return cat

revCat=cat_float(df,"TOTAL_PRICE")
df["RevCat"]=revCat
print df["RevCat"]
