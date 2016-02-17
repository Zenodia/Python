import json
import itertools
import operator
import math
import datetime

# Get median value, this is the mediam NOT average
def getMedian(values):
    sortedValues = sorted(values)
    length=len(values)
    half_length = length/2
    result=0
    if(length%2 == 1):
        result = values[int(math.ceil(half_length))]
    else:
        result = values[int(half_length)]
        result += values[int(half_length)+1]
        result /= 2
    return result

# Converting time format into DD:HH:MM:SS:MS
def date(data):
    msec = data % 1000
    data -= msec
    data = math.floor(data/1000)
    seconds = data % 60
    data -= seconds
    data = math.floor(data/60)
    minutes = data % 60
    data -= minutes
    data = math.floor(data/60)
    hours = data % 24
    data -= hours
    data = math.floor(data/24)
    days = data % 7
    time = "%u:%u:%u:%u:%u"%(days, hours, minutes, seconds, msec)
    return time
    #t = datetime.datetime.fromtimestamp(float(data)/1000000.0)
    #fmt = "%j days %Hh:%Mm:%Ss"
    #rep=t.strftime(fmt0

def by_half_hour(data):
    nb_half_hour=0
    divider=1000*60*30
    return data/divider
 
# Get activity vs timestamp for per unique client_id per day using dictionary
def getActiveTime(client_agenda):
    #print client_agenda
    nb_events = len(client_agenda)
    time_start=0 
    time_stop=0 
    active=0
    calculate=0
    cumulated_time=0
    view_loaded = 0
    for event in client_agenda:
        if (event['event_type'] == "session.start") or (event['event_type'] == "session.resume"):
            active=1
            time_start=event['timestamp']
        if (event['event_type'] == "ViewLoaded"):
            view_loaded+=1
        if (event['event_type'] == "session.stop") or (event['event_type'] == "session.pause"):
            calculate=1
            time_stop=event['timestamp']
        if (calculate==1) and (active==1) and (view_loaded>0):
            #print "%s:%s" % (time_stop, time_start)
            if( ( (time_stop != 0) and (time_start != 0) ) and (time_stop>time_start) ):
                cumulated_time += (time_stop - time_start)
            calculate=0
            time_stop=0 
            time_start=0
            view_loaded=0
    return cumulated_time


# Fetch the raw data from the json file
from pprint import pprint
with open('sample_data.json') as data_file:
    rawdata = json.load(data_file)

data = rawdata

# group the data per client
from operator import itemgetter
list_of_event_per_client=[]
for key,group in itertools.groupby(data,operator.itemgetter("client_id")):
    list_of_event_per_client.append(sorted(list(group), key=itemgetter('timestamp')))
#print list_of_event_per_client[0]
# get the active time of the clients
list_of_integrated_time=[]
for client in list_of_event_per_client:
    if len(client) < 2:
        continue
    value = getActiveTime(client)
    if ( (value > 2000) and (value<1000*60*60*24) ):
        list_of_integrated_time.append(value)

#print list_of_integrated_time
list_of_integrated_time=sorted(list_of_integrated_time)
median_time = getMedian(list_of_integrated_time)
median_time_human = date(median_time)
average_time = date(sum(list_of_integrated_time)/len(list_of_integrated_time))

print "integrated time sampled : "
print list_of_integrated_time
print "Consistancy - number of client from the list of time : %u" % len(list_of_integrated_time)
print "Median of integrated time : %s" % median_time_human
print "Average of integrated time : %s" % average_time


# plot time histogram with active time distrubution
convert=[]
for i in list_of_integrated_time:
    convert.append(i/1000/60/15)

import matplotlib.pyplot as plt
# 24*4 is how many times of 15 mins you have per day
n, bins, patches = plt.hist(convert, 24*4, normed=0, log=1, facecolor='b', alpha=0.5)
plt.xlabel('time (15 min)')
plt.ylabel('#')
plt.title('Active time distribution')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 24*4, 0, 1000])
plt.axis('tight')
plt.grid(True)
plt.show()
#plt.plot(list_of_integrated_time, )
#plt.show()

