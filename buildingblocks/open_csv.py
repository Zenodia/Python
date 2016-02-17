import csv
import os
import sys
import fileinput
d={}
filename='../data/test.csv'
with open(filename) as f:
    
    for line in f:
        #print line
        #print type(line)
        ls=line.split(';')
        d[ls[0]]=ls[1:]
print d.keys()

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

#writing the Dictionary back to csv file and name it outfile
with open('outfile.csv','wb') as c:
    w=csv.writer(c)
    for k,v in new_d.items():
        w.writerow([k,v])
c.close()
f.close()
    
    
    
