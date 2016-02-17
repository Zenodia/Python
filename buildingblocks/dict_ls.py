# practice on dictionary
import itertools
import operator
d={2:"two",1:"one",3:"three"}
print d.items() # print the items inside the dictionary
print d.iteritems() # cannot directly print need a for loop to print it
# use for loop to print one item at a time
for item in d.iteritems():
    print item

# accessing a item within a dictionary
print d[1] # using key
# using for loop to go through each k,v pair within a dictionary
for k,v in d.iteritems():
    print k,v
# update (add) items into the existing dictionary
d.update({4:"four"})
print d

# using lambda function to change the dictionary
def dict_fun(f,d):
    # for a given function f, change each corresponding value in d
    for k,v in d.iteritems():
        d[k]=f(v)
    return d

print dict_fun(lambda x: x[0], d) # take the 1st letter inside value string

#sort the dictionary by its keys
import collections
od=collections.OrderedDict(sorted(d.items()))
print od
print sorted(d) # print sorted d will only print keys
print sorted(d.values()) # pritn sorted dict by its values


# having a simple list consist of tuples
things=[ ("animal","bear"), ("animal","duct"), ("plant","cactus"),("vehicle","speed boat"), ("vehicle","school bus")]
# how to group them by the 1st item within each tuple ?
from itertools import groupby
for key, groups in groupby(things, lambda x:x[0]): # x[0] is the 1st item in the tuple
    for thing in groups:
        print "A %s is a %s." % (thing[1], key)
    print " "
    
# what about a list full of dictionaries ?
data=[{"fname":"Brian","lname":"Jons","uid":1003},
      {"fname":"David","lname":"Beazley","uid":1002},
      {"fname":"john","lname":"Cleese","uid":1001},
      {"fname":"Big","lname":"jones","uid":1004}]
from operator import itemgetter
rows_by_fname=sorted(data,key=itemgetter("fname"))
row_by_uid=sorted(data, key=itemgetter("uid"))

# print each uid and their names
# get the data by their uid value
#print data[0]["uid"] # this is how you get the value within a list of dictionaries
# get uid per row
index=[]
for k,grp in itertools.groupby(data, key=itemgetter("uid")):
    temp=[k,list(grp)]
    print temp # turn into [k,list(grp)]
    index.append(temp) # append to the empty list
index=sorted(index, key=lambda x: x[0]) # sort by the 1st element which is the key k=uid
print dict(index)

# if you have a list consist of tuples
tplist=[(1,"one"),(3,"three"),(2,"two"),(4,"four")]
# you can directly turn it into a dictionary
print dict(tplist)
# similary if you have a list of two paired list
lslist=[[1,"one"],[2,"two"],[3,"three"],[4,"four"]]
# go through them to convert them to tuples
length=len(lslist)
tpl=[]
for i in range(0,length):
    tp=tuple(lslist[i])
    #print tp # this is how you convert list of paired items into tuples and then convert them into dictionary
    tpl.append(tp)
print tpl
print dict(tpl)
