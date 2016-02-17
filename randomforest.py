import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from math import e
import csv

"""
1.
The only things you are allowed to write at top level is
import statements and constants.
Also, constants should be in all CAPS.

2.
All numbers are magical, except for 0 and 1.
Better put in into a constant or function argument.

3.
Importing is executing. This is why you don't want stuff executing automatically, by being at the top level.
"""

number = preprocessing.LabelEncoder()
df=pd.read_csv('./data/PurchaseIE.csv', sep=";", parse_dates=True, decimal=".", header=0)
df=df.drop(['avgTime'],axis=1)
#print df.dtypes

def convert(data):
    number = preprocessing.LabelEncoder()
    data['medium'] = number.fit_transform(data.medium)
    data['Device'] = number.fit_transform(data.Device)
    
    data=data.fillna(0)
    return data

df=convert(df)
#print df.tail()

df=df.drop(["CookieID"],axis=1)
#print df.head()

def preprocess(dfr):
    #split into training and validation sets

    dfr['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    train, test = dfr[dfr['is_train']==True], dfr[dfr['is_train']==False]
    return train, test


train,validate=preprocess(df)
#print train.head()
#print validate.head()

#create classifier for prediction

collist_t=list(train)
collist_v=list(validate)
collist_t.remove("Label")
collist_v.remove("Label")
x_train=train[collist_t]
x_validate=train['Label']
y_train=validate[collist_v]
y_validate=validate["Label"]

#print "x_train head", x_train.head()
#print "x_validate head", x_validate.head()
#print "y_train head", y_train.head()
#print "y_validate head", y_validate.head()
#print "y_validate is of type" , type(y_validate)
#print "x_train",x_train
#print "x_validate", x_validate


#fit randomforest algorithm with training data
#first create randomforest object
def create_random_forest(x_train=x_train, x_validate=x_validate, y_train=y_train, y_validate=y_validate, nr_trees=20):
    model=RandomForestClassifier(n_estimators=nr_trees)
    model.fit(x_train,x_validate)
    predict=model.predict(y_train)
    pred_p=model.predict_proba(y_train)
    print pred_p
    print "pred_p is of type" , type(pred_p)

    return model, pd.DataFrame(y_validate), predict, pred_p

#y_validate.to_csv('actual.csv', sep='\t')
#convert y_validate pandas series to ndarray and zip to output file

#write prediction to csv
#np.savetxt('prob.txt', pred_p, fmt="%.2f")
#np.savetxt('pred.txt', predict, fmt='%s')
"""
if __name__ == '__main__':
    main()
"""
