# ======== runMinHashExample =======
# This example code demonstrates comparing documents using the MinHash
# approach. 
#
# First, each document is represented by the set of shingles it contains. The
# documents can then be compared using the Jaccard similarity of their 
# shingle sets. This is computationally expensive, however, for large numbers
# of documents. 
#
# For comparison, we will also use the MinHash algorithm to calculate short 
# signature vectors to represent the documents. These MinHash signatures can 
# then be compared quickly by counting the number of components in which the 
# signatures agree. We'll compare all possible pairs of documents, and find 
# the pairs with high similarity.
#
# The program follows these steps:
# 1. Convert each test file into a set of shingles.
#    - The shingles are formed by combining three consecutive words together.
#    - Shingles are mapped to shingle IDs using the CRC32 hash.
# 2. Calculate all Jaccard similarities directly.
#    - This is ok for small dataset sizes. For the full 10,000 articles, it
#      takes 20 minutes!
# 3. Calculate the MinHash signature for each document.
#    - The MinHash algorithm is implemented using the random hash function 
#      trick which prevents us from having to explicitly compute random
#      permutations of all of the shingle IDs. For further explanation, see
#      section 3.3.5 of http://infolab.stanford.edu/~ullman/mmds/ch3.pdf
# 4. Compare all MinHash signatures to one another.
#    - Compare MinHash signatures by counting the number of components in which
#      the signatures are equal. Divide the number of matching components by
#      the signature length to get a similarity value.
#    - Display pairs of documents / signatures with similarity greater than a
#      threshold.

from __future__ import division
import os
import re
import random
import time
import binascii
from bisect import bisect_right
from heapq import heappop, heappush

# This is the number of components in the resulting MinHash signatures.
# Correspondingly, it is also the number of random hash functions that
# we will need in order to calculate the MinHash.
numHashes = 10;

# You can run this code for different portions of the dataset.
# It ships with data set sizes 100, 1000, 2500, and 10000.
numDocs = 100
dataFile = "./data/articles_" + str(3) + ".train"
truthFile = "./data/articles_" + str(numDocs) + ".truth"

# =============================================================================
#                  Parse The Ground Truth Tables
# =============================================================================
# Build a dictionary mapping the document IDs to their plagiaries, and vice-
# versa.
plagiaries = {}

# Open the truth file.
f = open(truthFile, "rU")

# For loop went through each line of the file and only take the 1st element
for line in f:
  
  # Strip the newline character, if present.
  if line[-1] == '\n':
      line = line[0:-1]
      
  docs = line.split(" ")
    
  # Map the two documents to each other.
  plagiaries[docs[0]] = docs[1]
  plagiaries[docs[1]] = docs[0]
  

# =============================================================================
#               Convert Documents To Sets of Shingles
# =============================================================================



# The current shingle ID value to assign to the next new shingle we 
# encounter. When a shingle gets added to the dictionary, we'll increment this
# value.
curShingleID = 0

# Create a dictionary of the articles, mapping the article identifier (e.g., 
# "t8470") to the list of shingle IDs that appear in the document.
docsAsShingleSets = {};
  
# Open the data file.
f = open(dataFile, "rU")

docNames = []

t0 = time.time()

totalShingles = 0

for i in range(0, numDocs):
  
  # Read all of the words (they are all on one line) and split them by white
  # space.if needed,use rm_punctuation.py to clean b4 bring in here.
  words = f.readline().split(" ") 
  #print " %s_th document , the words are: %s" %(str(i),words)
  # Retrieve the article ID, which is the first word on the line.  
  docID = words[0]
  
  # Maintain a list of all document IDs.  
  docNames.append(docID)
    
  del words[0]  
  
  # 'shinglesInDoc' will hold all of the unique shingle IDs present in the 
  # current document. If a shingle ID occurs multiple times in the document,
  # it will only appear once in the set (this is a property of Python sets).
  shinglesInDoc = set()
  
  # For each word in the document...
  for index in range(0, len(words) - 2):
    # Construct the shingle text by combining 3 words together
    # hence the usable total length of the document is len(doc)-2
    shingle = words[index] + " " + words[index + 1] + " " + words[index + 2]

    # Hash the shingle to a 32-bit integer.
    crc = binascii.crc32(shingle) & 0xffffffff
    
    # Add the hash value to the list of shingles for the current document. 
    # Note that set objects will only add the value to the set if the set 
    # doesn't already contain it. 
    shinglesInDoc.add(crc)
  
  # Store the completed list of shingles for this document in the dictionary.
  docsAsShingleSets[docID] = shinglesInDoc
  
  # Count the number of shingles across all documents.
  # the -2 is because we say the shingle is 3 words, so the lenth has to -2
  totalShingles = totalShingles + (len(words) - 2)
print "total shingles across al documents are %s" %str(totalShingles)
# Close the data file.  
f.close() 

# report how long shingling took
#print "\nShingling"+str(numDocs)+"docs took %.2f sec."(time.time()-t0)
print "\nAverage shingles per doc: %.2f" %(totalShingles/numDocs)
