# the baskets of items
"""rawdata=[{"basket1":["milk","coke","beer"]},{"basket2":["milk","pepsi","juice"]},{"basket3":["milk","beer"]},{"basket4":["coke","juice"]},{"basket5":["milk","pepsi","beer"]},{"basket6":["milk","coke","beer","juice"]},{"basket7":["coke","beer","juice"]},{"basket8":["beer","coke"]}]

rawdata=[{"b1":["A","B","C","E","F"]},{"b2":["B","C","D","E","F"]},{"b3":["A","C","D","E"]},{"b4":["A","C","D"]},{"b5":["A","B","C","D","E"]},{"b6":["B","D","F"]},{"b7":["A","C","E"]}]
"""
rawdata=[{"7191013652":["DayTrip","GOFR","FRGO","PlusLounge","Car"]},{"7201365421":["Cruise","GOKI","KIGO","breakfast"]},{"7201012543":["GOFR","FRGO","Daytrip"]},{"7104569875":["GOFR","Pet"]},{"2154656987":["FerryHotel","H:Legoland","GOFR","FRGO","restaurant:Metropolis","children","Ticket:LegoLand"]},{"7546985978":["DayTrip","GOFR","FRGO"]},{"7665456651":["Cruise","GOKI","KIGO","Cabin:Captainsview"]},{"7789878981":["DayTrip","GOFR","FRGO","Car"]}]
print rawdata
# the minsupport threshold
min_support_threshold=3

import itertools
from itertools import *
import operator

def label(data):
    d={}
    lst=[]
    l=len(data)
    k_ls=[i for i in xrange(l)]
    # flatten the backet items to create a unique set of items
    for i in range(0, l):
        for item in data[i].values():
            for i in itertools.chain(item):
                #print i
                lst.append(i)
    # create a unique set of items
    lst=list(set(lst))
    llst=len(lst)
    final_list=[]
    # create dictioary to relabel the unique item sets for A-priori pass one
    for i in range(0,llst):
        d[lst[i]]=i
        final_list.append(i)
        final_list=list(set(final_list))
    # return the dictionary with the labeled unique item sets
    return d,final_list
d,ls=label(rawdata)
d_sorted=sorted(d.items(), key=operator.itemgetter(1))
print " items maps to %s" %d_sorted

def data_to_label(data):
    l=len(data)
    data_d={}
    d,ls=label(data)
    basketmap={}
    #print data
    #print d
    for i in range(0,l):
        for k,v in data[i].iteritems():
            vl=len(v)
            value=[]
            for j in range(0,vl):
                value.append(d[v[j]])
        #print "basket %s map to integer %s "%(k, str(i))
        data_d[i]=value
        basketmap[k]=i
    print "basketmap : %s" %basketmap.items()
    return data_d

print data_to_label(rawdata)
print " above are data_to_label"

def pass1(dataset,dictionary,candidates, min_support):
    "Returns all candidates that meets a minimum support level"
    d={}
    fd={}
    l=len(dataset)
    m=len(candidates)
    ini=0
    freq_items=[]
    for i in range(0,m):
        ini=0
        for j in range(0,l):
            #print i
            #print dataset[j]
            if candidates[i] in dataset[j]:
                ini+=1
            d[i]=ini
    
    # return the dictionary with the labeled having only the frequent item
    for i in range(0,m):
        if d[i]>=min_support:
            fd[i]=d[i]
            freq_items.append(i)
    #print freq_items
    #print fd
    return d, fd, freq_items


d, ls=label(rawdata)
data=data_to_label(rawdata)

print data
# return frequent singletons via A-priori algorithm 1st time passing all baskets
d1,d2,l1= pass1(data,d,ls, min_support_threshold)
print "d1"
print d1
print "d2"
print d2
print "l1"
print l1

def pair_freq(f_items):
    length=len(f_items)
    pairs=[]
    for c in itertools.combinations(f_items,2):
        pairs.append(c)
    return pairs

#print pair_freq(l1)

def pass2(data, freqitems, minsupport):
    getpair=pair_freq(freqitems)
    lng=len(getpair)
    ldata=len(data)
    pair_d={}
    for i in range(0,lng):
        init=0
        for j in range(0,ldata):
            if getpair[i][0] in data[j] and getpair[i][1] in data[j]:
                init+=1
        pair_d[getpair[i]]=init
    # get pairs that pass the minsupport threshold
    final_pair={}
    for k in pair_d.keys():
        #print k, pair_d[k]
        if pair_d[k]>=minsupport:
            #print "if start for key %s" %str(k)
            final_pair[k]=pair_d[k]
            #print final_pair
        else:
           continue
    return final_pair,pair_d
#get frequent pair of items using pass 2 via A-priori algorithm
freq_item_pairs, all_pair_count= pass2(data, l1, min_support_threshold)
print "frequent item pairs:"
print freq_item_pairs
print " all pairs combination vs their counts: "
print all_pair_count

# get tripletons
def pass3(data,singleton,doubleton,minsupport):
    triple={}
    singleton_l=len(singleton)
    for i in range(0,singleton_l):
        for k,v in doubleton.iteritems():
            temp=list(chain.from_iterable([k]))
            #print "pass 3 temp with k,v : (%s, %s) in doubleton" % (k,v)
            #print temp
            tri=temp
            if singleton[i] not in k:
                #print singleton[i]
                tri.append(i)
                #print "pass 3 tri add singletons with singleton:%s"%str(singleton[i])
                tri=list(set(tri))
                tri=tuple(tri)
                triple[tri]=0
            
    #print "triple "
    #print  triple
    
    #count  tripletons
    ld=len(data)
    lt=len(triple.keys())
    print lt
    for key,value in triple.iteritems():
        init=0
        for j in range(0,ld):
            if key[0] in data[j] and key[1] in data [j] and key[2] in data[j]:
                init+=1
                key=tuple(set(key))
        triple[key]=init

    #get freq triples
    freq_triples={}
    for k,v in triple.iteritems():
            if v>=minsupport:
                freq_triples[k]=v
    return triple, freq_triples
        

tri, freq_tri=pass3(data, l1, all_pair_count, min_support_threshold)
print " triples : tri is "
print tri
print "freq triples : freq_tri is:"
print freq_tri

# create potential association rule pairs (x,y) -->z
# where (x,y) is frequent doubleton and z is freqent singletons and z!=x&z!=y
def get_asso_pairs(fq_i, fq_i_pair):
    asso_pairs={}
    
    for k,v in fq_i_pair.iteritems():
        print k
        for s in fq_i.keys():
            if s not in k:
                asso_pairs[k]=s
    return asso_pairs

print "association rule candidate: "
pairs_asso=get_asso_pairs(d2,freq_item_pairs)
print pairs_asso
# this confidence works on doubletons (x,y)--> singletons z
# feed pair_to_compute a tuple form such as ((x,y):z)from pairs_asso
def get_confidence(freq_i_pair, tri, pair_to_compute):
    #print pair_to_compute[0]
    #print pair_to_compute[1]
    confidence_d={}
    item1=list(pair_to_compute[0])
    item1=sorted(item1)
    item1=tuple(item1)
    #print " item1 is: "
    #print item1
    item1_support=freq_i_pair[item1]
    #item1=list(item1)
    #print type(item1)
    #print "item %s support :" % str(item1)
    #print item1_support
    item12=[i for i in item1]
    item12.append(pair_to_compute[1])
    item12=sorted(item12)
    item12=tuple(item12)
    print "item12 is:%s" %str(item12)
    #print "item12 is : "
    #print item12
    key="%s->%s"%(str(pair_to_compute[0]),str(pair_to_compute[1]))
    #print key
    #print tri
    item12_support=tri[item12]
    print "tri is%s " %str(tri)
    #print " item %s support is : " % str(item12)
    #print item12_support
    
    confidence_d[key]=float(item12_support)/item1_support
    return confidence_d

# get confidence of a pair of items i, j to compute confidence i--> j
#get one item in pairs_asso say {(1,2):3}
"""
for item in pairs_asso.iteritems():
    print "item is now : %s" %str(item)
    print "confidence is : "
    print get_confidence(freq_item_pairs,tri, item)
"""


# get confidence of any x->y , x and y are both single item
def confidence(f_single, f_pair,x,y):
    tp=(x,y)
    tp=tuple(sorted(tp))
    #print tp
    #print f_pair[tp]
    #print f_single[x]
    # confidence between x-->y is
    conf=float(f_pair[tp])/f_single[x]
    return conf

# get confidence of single item --> single item , ex: 4-->3
#print confidence(d1,all_pair_count,4,3)
single_conf=[]
for k in d2.keys():
    single_conf.append(k)

sinconf=len(single_conf)
for i in range(0,sinconf-1):
    print " confidence for item %s and %s: " %(single_conf[i], single_conf[i+1])
    print confidence(d1,all_pair_count, single_conf[i], single_conf[i+1])
#get the interest of pair --> single item , ex:(2,3)-->1
"""
def get_interest(fq_i, fq_i_pair,triples, pairs_to_interest,dat):
    interest_d={}
    item1=pairs_to_interest[0]
    item2=pairs_to_interest[1]
    l=len(dat)
    key="%s->%s"%(str(item1),str(item2))
    confidence=get_confidence(fq_i_pair,triples, pairs_to_interest)
    item2_support=fq_i[item2]
    item2_fraction=item2_support/float(l)
    interest_d[key]=float(confidence[key]-item2_fraction)
    return interest_d    
print " interest for i--> j is :"
print get_interest(d2,all_pair_count,tri,((2,3),1),data)
"""


