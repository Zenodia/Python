from __future__ import division
import itertools
import re

# a shingle in this code is a string with K-words
K = 3

dataFile="./data/blog"+".txt"
documents=open(dataFile,"rU")
def jaccard_set(s1, s2):
    " takes two sets and returns Jaccard coefficient"
    u = s1.union(s2)
    i = s1.intersection(s2)
    return len(i)/len(u)

def make_a_set_of_tokens(doc):
    """makes a set of K-tokens"""

    # replace non-alphanumeric char with a space, and then split but keep the white 
    tokens = re.sub("[^\w]", " ",  doc).split()

    sh = set()
    for i in range(len(tokens)-K):
        t = tokens[i]
        for x in tokens[i+1:i+K]:
            t += ' ' + x 
        sh.add(t)
    return sh

shingles = []
# handle documents one by one
# makes a list of sets which are compresized of a list of K words string
for doc in documents:
    # makes a set of tokens
    # sh = set([' ', ..., ' '])
    sh = make_a_set_of_tokens(doc)

    #print " the sets of tokens are %s" %list(sh)
    # shingles : list of sets (sh)

    shingles.append(sh)
    #print " the singles are %s" % shingles

#print("shingles=%s") %(shingles)
print " total length of shingles are %.2f" %len(shingles)

combinations = list( itertools.combinations([x for x in range(len(shingles))], 2) )
print("combinations=%s") %(combinations)

# compare each pair in combinations tuple of shingles
for c in combinations:
    i1 = c[0]
    i2 = c[1]
    jac = jaccard_set(shingles[i1], shingles[i2])
    print("%s : jaccard=%s") %(c,jac)

documents.close()
