# the baskets of items
rawdata=["A","B","C","D","E","F","G","H"]
print rawdata

singletons=["A","B","C","D","E","F"]
doubletons=[("A","B"),("A","C"),("A","D"),("B","C")]
singleton_NB=[]
doubleton_NB=[]
tripleton_NB=[]
for item in rawdata:
    if item not in singletons:
        singleton_NB.append(item)
print " singletons in negative border are : %s" % singleton_NB

import itertools
from itertools import *
import operator

ldata=len(rawdata)
for c in itertools.combinations(rawdata,2):
    if c not in doubletons and c[0] in singletons and c[1] in singletons:
        doubleton_NB.append(c)

doubleton_NB=sorted(list(set(doubleton_NB)))
print "doubleton in negative borders are: %s " %doubleton_NB

for c in itertools.combinations(rawdata,3):
    if (c[0],c[1]) in doubletons and (c[1],c[2]) in doubletons and (c[0],c[2]) in doubletons:
        tripleton_NB.append(c)

tripleton_NB=sorted(list(set(tripleton_NB)))
print "tripletons in negative borders are : %s" %tripleton_NB




