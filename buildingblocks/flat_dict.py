import itertools
from itertools import *
import operator
from operator import itemgetter

test_dict=[{(1,3,4):3}]
ls=[test_dict.iteritems(), key=itemgetter(0), reversed=True]
print ls
