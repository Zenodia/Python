import httpagentparser

#print httpagentparser.simple_detect(s)

#print httpagentparser.detect(s)
import json
from pprint import pprint
import itertools
import operator
from operator import itemgetter
import math
import datetime
# import tealium.json file to python and extract sample data
data = []
with open('./data/tealium.json') as f:
    for line in f:
        data.append(json.loads(line))

print " length of the data : %d" % len(data)
#extract sample data by name of the key , ex : "visitorid"
#print data[0]["visitorid"]
#sample=data[0]["useragent"]
#print type(s)

#print httpagentparser.simple_detect(s)

#parse all browser data from useragent
#print "before"
#print data[0]["useragent"]

#convert useragent into simple browser version

l=len(data)
for i in range(0,l):
    s=httpagentparser.simple_detect(data[i]["useragent"])
    data[i]["useragent"]=s

#print "after"
#print data[0]["useragent"]
    
# count unique users
num_visitorid=[]
for i in range(0,l):
    num_visitorid.append(data[i]["visitorid"])
num_visitorid=list(set(num_visitorid))

print " number of unique visitorid : %d" % len(num_visitorid)

# get list of event per_visitorid
gpby_vid={}
for key,group in itertools.groupby(sorted(data),operator.itemgetter("visitorid")):
    gpby_vid[key]=list(group)
    

#print type(gpby_vid["015014ec67df001848a322999e9e0606d0033065009dc"][0])
#print gpby_vid["015014ec67df001848a322999e9e0606d0033065009dc"][0]["eventtime"]
#print type(gpby_vid)


# see how many visitor id has only one event
shortdict={}
for vid in num_visitorid:
    ls=[]
    for k,v in gpby_vid[vid][0].iteritems():
        if k=="useragent":
            temp=(gpby_vid[vid][0]["eventtime"], gpby_vid[vid][0]["useragent"])
            ls.append(temp)
    shortdict[vid]=ls

#print shortdict["015014ec67df001848a322999e9e0606d0033065009dc"][0][1][0]
#print shortdict["015014ec67df001848a322999e9e0606d0033065009dc"][0][1][1]
#print len(shortdict["015014ec67df001848a322999e9e0606d0033065009dc"]

# get list of devices used by visitor
device=[]
browser=[]
for vid in num_visitorid:
    for item in shortdict[vid][0]:
        device.append(shortdict[vid][0][1][0])
        browser.append(shortdict[vid][0][1][1])
device=sorted(list(set(device)))
#print device
browser=sorted(list(set(browser)))
#print browser
device_d={}
browser_d={}
for dev in device:
    count=0
    for vid in num_visitorid:
        if shortdict[vid][0][1][0]==dev:
            count+=1
    device_d[dev]=count
for bro in browser:
    cnt=0
    for vid in num_visitorid:
        if shortdict[vid][0][1][1]==bro:
            cnt+=1
            #if shortdict[vid][0][1][1]=="Microsoft Internet Explorer 9.0":
                #print vid
    browser_d[bro]=cnt

#print device_d
print browser_d
#print shortdict
"""
for key,values in gpby_vid.iteritems():
    ls=[]
    #print type(values[0])
    for v in values[0].iteritems():
        if v=="useragent" or v=="eventtime":
            temp=(v["useragent"], v["eventtime"])
            ls.append(temp)
    shortdict[key]=ls


"""
    

        
#print groupby_visitorid[0][0]
#print len(groupby_visitorid[0][0])

