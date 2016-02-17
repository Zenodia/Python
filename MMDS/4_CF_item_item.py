import numpy as np
import numpy.ma as ma
import itertools
import operator
import itertools
import collections
import math
from scipy import spatial
from collections import Counter

#type in the Utility matrix
U=np.array([[1.,0,3,0,0,5,0,0,5,0,4,0],[0,0,5,4,0,0,4,0,0,2,1,3],[2,4,0,1,2,0,3,0,4,3,5,0],[0,2,4,0,5,0,0,4,0,0,2,0],[0,0,4,3,4,2,0,0,0,0,2,5],[1,0,3,0,3,0,0,2,0,0,4,0]])
# type in the empty=0 and mask it with 1 , which will become -- in the resulting matrix
mU=ma.masked_array(U,mask=[[0,1,0,1,1,0,1,1,0,1,0,1],[1,1,0,0,1,1,0,1,1,0,0,0],[0,0,1,0,0,1,0,1,0,0,0,1],[1,0,0,1,0,1,1,0,1,1,0,1],[1,1,0,0,0,0,1,1,1,1,0,0],[0,1,0,1,0,1,1,0,1,1,0,1]])

N=2 # size of the neighborhood given by the question
# tyope in the Goal- (1) which user (2) which row would like to predict the missing ratings
user=5
row=1

print "Utility Matrix U is :"
print U
print "masked matrix mU is:"
print mU
l,m=U.shape # get the dimension of the Utility matrix,here l=6 by m=12 
row_mean=np.zeros(l)

for i in range(0,l):
    row_mean[i]=mU[i].mean() # compute row means using masked mU matrix

U_update=np.zeros((l,m))
for i in range(0,l):
    for j in range(0,m):
        if U[i][j]==0:
            U_update[i][j]=0
        else:
            U_update[i][j]=U[i][j]-row_mean[i]

print "update the U matrix and substract the row mean : U_update"
print U_update

#result=1-spatial.distance.cosine(U_update[0],U_update[1])
#print result

# compute pair-wised cosine distance between any row x, y
def cosineDist(x,y):
    return 1-spatial.distance.cosine(x,y)

#create consine similarity dictionary called sim_dict
sim_dict={}
for i in range(0,l):
    for j in range(0,l):
        tp=(i+1,j+1)
        sim_dict[tp]=cosineDist(U_update[i],U_update[j])
#sort the cosine similarity dictionary by keys 
sim_dict=collections.OrderedDict(sorted(sim_dict.items()))

#d=Counter(sim_dict)
#print d.most_common()        
#print type(sim_dict.keys()[0])

# give a row number and create the begining and ending in order to product a subdictionary
def begin_end(rn):
    lst=[]
    for i in range(0,l):
        tup=(rn,i+1)
        lst.append(tup)
    print lst
    return lst[0], lst[-1]
begining, ending=begin_end(row)
#print begin_end(2)

# product the subdictionary by slicing the sim_dict with begining and end provided by above 
def get_subset_simdict(d, begin, end):
    result={}
    for k, v in d.iteritems():
        if k>=begin and k<=end:
            result[k]=v
    return result


#resulting subdictionary
subd=get_subset_simdict(sim_dict, begining,ending)
print " subset of the similarity dictionary is sim_dict :"
print subd
#prepare the removable tuple with the form (i,i)
remove_tp=(row,row)
print remove_tp
# get the topN neighbors within that subdictionary

def get_max(subdict,topN,rm_tp):
    topN_list={}
    max_dict=Counter(subdict)
    for k,v in max_dict.most_common(topN+1):
        topN_list[k]=v
    del topN_list[rm_tp]
    return topN_list
top_neighbor=get_max(subd, N,remove_tp)
print "top %d neighborgs are: " %N
print top_neighbor

#predicting rating for user 5 and row 1
pred={}
#retrieve corresponding row number=(dictionary 2nd tuple -1) and column number=(user-1)
c=user-1

rowkeys=top_neighbor.keys()
rowvalues=top_neighbor.values()

ithrow1=rowkeys[0][1]-1
#print ithrow1
ithvalue1=rowvalues[0]
#print ithvalue1
ithrow2=rowkeys[1][1]-1
#print ithrow2
ithvalue2=rowvalues[1]
#print ithvalue2

itehvalue2=rowvalues[1]
# retrieve original rating from similar rows here it is row 3 (row2) and row 6( here it is row 5) respectively for user 5
weight1=U[ithrow1][c] # retrieve original rating for row 3=row 2 as weight 1 for ithvalue1
weight2=U[ithrow2][c] # retrieve original rating for row 6=row 5 as weight 2 for ithvalue2

# predicted rating for user 5 is
pred_rating=(ithvalue1*weight1+ithvalue2*weight2)/(ithvalue1+ithvalue2)
print " user %d's %d-th row predicted rating is : " %(user, row)
print pred_rating

        


    
    



