import itertools
l = [1,2,3]
comb = []
for i in range(len(l)):
   comb += itertools.combinations(l,i+1)
   print " %s-th value for com is now : %s) " %(i, comb)

#another example
items = ['a', 'b', 'c']
for c in itertools.combinations(items, 2):
     print "exploit all combination of 2 items inside of a item list "
     print(c)

for c in itertools.combinations_with_replacement(items, 3):
    print "combination of 3 items picked within items with replacement"
    print(c)
