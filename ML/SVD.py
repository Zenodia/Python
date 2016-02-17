import numpy as np
import csv
import os
import sys
import fileinput
import itertools
from itertools import *
import operator
import collections
from scipy import linalg
d={}
filename='../data/100000.csv'
with open(filename) as f:
    
    for line in f:
        #print line
        #print type(line)
        ls=line.split(';')
        d[ls[0]]=ls[1:]
#print d.keys()

new_d={}
for k,v in d.iteritems():
    #print len(v)
    temp=[]
    for val in v:
        #print val
        #temp=[]
        if val!='NULL':
            temp.append(val)
        #print temp
    new_d[k]=temp
#print new_d.keys()
#print new_d.values()

min_support_threshold=3500

k_ls=[k for k in new_d.keys()]
rk=len(k_ls)

#relabel the booking number from 0 to however many bookings we have
def basket_label(data):
    b_label={}
    k_ls=[k for k in data.keys()]
    l=len(k_ls)
    for i in range(0,l):
        b_label[i]=k_ls[i]
    return b_label
    
labelledBookings= basket_label(new_d)

#print labelledBookings

#get list of unique and total item sets
def unique_items(data_d, ls_keys):
 uniq_items=[]
 for k,v in ls_keys.iteritems():
     #print "k is ",k
     #print "v is", v
     for val in data_d[v]:
         #print "val is ", val
         if val!='' and val!="NULL" and val!='\r\n':
            uniq_items.append(val)
 uniq_items=list(set(uniq_items))
 return uniq_items

ls_items=unique_items(new_d, labelledBookings)

num_items=len(ls_items)
print " number of items being processed is :" , num_items
print " number of bookings being processed is:", len(labelledBookings)
rows=len(labelledBookings)
matrix_dim=(rows, num_items)
A=np.zeros(matrix_dim)
#print A

sort_items=sorted(ls_items)
print "sorted items: ", sort_items
#print sort_items
for i in range(0, rows):
    for j in range(0,num_items):
        if sort_items[j] in new_d[labelledBookings[i]]:
            A[i][j]=1
#print A
    
# type in needed # of concept
concept=10
# if we want to project a user q's preference, we simply Vh.dot(q)
#q=np.array([[5,0,0,0,0]])


M,N = A.shape
print "shape of matrix A is :"
print
print A.shape
U,s,Vh = linalg.svd(A)
Sig = linalg.diagsvd(s,M,N)
U, Vh = U, Vh
print " U is :"
U_reshape=U[:,:concept]
print -U_reshape
print 
print " diagnal matrix is :"
Sig_reshape=Sig[:concept,:concept]
print Sig_reshape
print
print "V is : "
Vh_reshape=Vh[:concept,:]
print -Vh_reshape
print
#print "user q's concept space projection with SVD solution is :"
#print -Vh_reshape.dot(q.T)
#print
print "check computation is correct, ie see if SVD =A "
print U.dot(Sig.dot(Vh)) #check computation
#create Pseudoinverse
print
print" U transpose is :"
print U.T
#print A.shape
"""get Sigma matrix inverse is simply (1/Sigma) skipping zero diagnal entries"""
def get_invDiagnal(d_matrix):
    m,n=d_matrix.shape
    new_m=np.zeros((m,n))
    for i in range(0,n):
        if d_matrix[i][i]!=0:
            new_m[i][i]=1/(d_matrix[i][i]) # d_matrix[i][i]=Sigma
    return new_m

inv_Sig=get_invDiagnal(Sig)
print
print "the inverse of the diagnal matrix inv_Sig is "
print inv_Sig
#compute Moore-Penrose pseudoinverse
print
print "Moore-Penrose pseudoinverse matrix for input matrix A is : "
print U.T.dot(inv_Sig.dot(Vh))


