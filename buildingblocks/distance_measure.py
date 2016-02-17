from scipy import spatial
import numpy as np
# distance measure by two vectors=np arrrays
u1=np.array([[1,0.25,0,0,0.5,0]])
u2=np.array([[0.75,0,0,0.2,0.4,0]])
u3=np.array([[0,0.1,0.75,0,0,1]])

print "Cosine Distance measure for vector %s , %s is :" %(u1,u2)
print 1-spatial.distance.cosine(u1,u2)


v1=np.array([[1,1,0,1,1,0]])
v2=np.array([[0,1,1,0,0,0]])
j_dist=spatial.distance.jaccard(v1,v2)
j_sim=1-j_dist
print "Jaccard distance for %s , %s is : " %(v1,v2)
print j_dist
print "Jaccard Similarity for the same two vectors is:"
print "noted that Jaccard Similarity= 1-Jaccard Distance"
print j_sim

s1="zeno"
s2="zeno charpy"
# non vector Jaccard distance
# Jaccard distance for strings , NOT integer as strings, 11000000 wont work
def DistJaccard(str1,str2):
    #using below for character_set=set(strings)
    #eg: str=zenodi-->character_set=['z','e','n','o','d','i','a']
    str1=set(str1)
    print str1
    str2=set(str2)
    print str2
    #use below for word_set=set(strings.split())
    # eg:zeno charpy-->word_set=['zeno','charpy']
    """
    str1=set(str1.split())
    str2=set(str2.split())
    """
    return float(len(str1&str2))/len(str1|str2)

print DistJaccard(s1,s2)




        
