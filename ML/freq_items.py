import csv
import os
import sys
import fileinput
import itertools
from itertools import *
import operator
import collections
d={}
filename='../data/IEtime.csv'
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

min_support_threshold=100

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
         if val!='' and val!="NULL":
            uniq_items.append(val)
 uniq_items=list(set(uniq_items))
 return uniq_items

ls_items=unique_items(new_d, labelledBookings)

num_items=len(ls_items)
print " number of items being processed is :" , num_items
print " number of bookings being processed is:", len(labelledBookings)
"""
for m in range(0,num_items):
    print type(ls_items[m])
    print ls_items[m]


for keys,vals in new_d.iteritems():
    lv=len(vals)
    print keys
    print type(vals)
    for j in range(0,lv):
        if vals[j]=='':
            print "empty strings"
        else:
            print type(vals[j]), "vals is :", vals[j]
"""

def pass1(d_data, d_keys, item_lists,min_s):
    d_item_cnt={}
    m=len(item_lists)
    l=len(d_data)
    for i in range(0,m):
        ini=0
        for j in range(0,l):
            if item_lists[i] in d_data[d_keys[j]]:
                ini+=1
                d_item_cnt[item_lists[i]]=ini
    #make a new dictionary to count the items the reach the min_supports
    pass1_d={}
    for k,v in d_item_cnt.iteritems():
        if v>=min_s:
            pass1_d[k]=v
    return d_item_cnt, pass1_d

            
singleton_d, pass1_dict=pass1(new_d,labelledBookings,ls_items, min_support_threshold)

with open('../outputfile/pass1_allitemscnt.csv','wb') as c1:
    w=csv.writer(c1)
    for s1,t1 in singleton_d.items():
        w.writerow([s1,t1])
c1.close()

#print "singletons_d all singletons", singleton_d
#print "pass1 survivors" , pass1_dict

def make_pairs(f_items):
    ls_items=f_items.keys()
    length=len(ls_items)
    pairs=[]
    for c in itertools.combinations(ls_items,2):
        pairs.append(c)
    return pairs
pairs=make_pairs(pass1_dict)

def make_triples(f_d):
    lsItems=f_d.keys()
    lth=len(lsItems)
    triples=[]
    for d in itertools.combinations(lsItems,3):
        triples.append(d)
    return triples
triples= make_triples(pass1_dict)
#print type(pairs), pairs
#print type(triples)

lpass1=len(pairs)
for it in range(0,lpass1):
    print type(pairs[it])
    p=list(pairs[it])
    print type(p)
    print p[0],p[1]
    print type(p[0])


def pass2(ori_d, pair_ls, basket_d, min_sp):
    pair_l=len(pair_ls)
    data_l=len(ori_d)
    pair_cnt_d={}
    for s in pairs:
        init=0
        for t in range(0,data_l):
            if s[0] in ori_d[basket_d[t]] and s[1] in ori_d[basket_d[t]]:
                init+=1
                pair_cnt_d[s]=init
    pass2_d={}
    for k2,v2 in pair_cnt_d.iteritems():
        if v2>=min_sp:
            pass2_d[k2]=v2
    return pair_cnt_d, pass2_d
pair_cnt, pass2_dict = pass2(new_d, pairs, labelledBookings, min_support_threshold)
#print pair_cnt
#print pass2_dict
# convert pairs item count to csv named c2

with open('../outputfile/pass2_allpairscnt.csv','wb') as c2:
    w=csv.writer(c2)
    for s2,t2 in pair_cnt.items():
        w.writerow([s2,t2])
c2.close()

def pass3(od, tri, bd, min_su):
    tri_l=len(tri)
    dl=len(od)
    tri_cnt_d={}
    for a in tri:
        initial=0
        for b in range(0, dl):
            if a[0] in od[bd[b]] and a[1]in od[bd[b]] and a[2] in od[bd[b]]:
                initial+=1
                tri_cnt_d[a]=initial
    pass3_d={}
    for k3,v3 in tri_cnt_d.iteritems():
        if v3>=min_su:
            pass3_d[k3]=v3
    return tri_cnt_d, pass3_d
tripletons, pass3_dict=pass3(new_d,triples, labelledBookings, min_support_threshold)
print pass3_dict
with open('../outputfile/pass3_alltricnt.csv','wb') as c3:
    w=csv.writer(c3)
    for s3,t3 in tripletons.items():
        w.writerow([s3,t3])
c3.close()

num_bok=len(labelledBookings)
"""
for trik,triv in pass3_dict.items():
    print type(trik)
    print list(trik)
    print trik[0], type(trik[0])
"""

            

    
