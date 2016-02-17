import json
from pprint import pprint
with open('sample_data.json') as data_file:
    data = json.load(data_file)

#converting time format in the whole data set
import datetime
def to_date(i, data):
    s = data[i]["timestamp"]
    t = datetime.datetime.fromtimestamp(float(s)/1000.0)
    fmt = "%Y-%m-%d %H:%M:%S"
    rep=t.strftime(fmt)
    return rep

#create newdata replacing timestamp format
newdata=data
length=len(newdata)
for i in range(0,length):
    d=newdata[i]
    d.update((k,to_date(i,newdata)) for k,v in d.iteritems() if k=="timestamp")

# get a list of unique event types
new_list=[]
for i in range(0, length):
    new_list.append(newdata[i]["event_type"])

unique_events=list(set(new_list))    
unique_events.sort()

# get k=event_type, v=client_id in a new dict called event_id_pair
event_id_list=[]
event_id_dict={}
tuple_list=[]
for j in range(0, length):
    event_id_dict=[newdata[j]["event_type"], newdata[j]["client_id"]]
    event_id_list.append(event_id_dict)
    event_id_tuple=tuple(event_id_dict)
    tuple_list.append(event_id_tuple)

#sort the list of tuple pairs
tuple_list=sorted(tuple_list, key=lambda tp:tp[0])

import itertools
import operator

for key,group in itertools.groupby(tuple_list,operator.itemgetter(0)):
    print(key, len(list(set(group))))

