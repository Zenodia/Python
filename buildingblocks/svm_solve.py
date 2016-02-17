import numpy as np
from scipy import linalg
from math import *
#finding wx+b=0 lines, in 2 dimensions, we need 3 support vectors=3 points
#Step1: pick 3 points, either 2 positive +1 negative or 2 negative +1 positive
# below is picking 2 positive points +1 negative points
# Step 2:solve the equation of (w1,w2,b).dot (x,y,1)=(1,1,-1)
#Step3: pick r=|w| with the smallest length
A=np.array([[5,4,1],[8,3,1],[7,2,1]])
#print " two positive points +1 negative point making matrix A:"
#print A
c=np.array([1,1,-1])
#print "two positive points +1 negative point make vector c=[1,1,-1]"
#print c
x=np.linalg.solve(A,c)
print "w1 is :"
print x[0]
print "w2 is:"
print x[1]
print "b is:"
print x[2]
print "margin r=1/|w| is : pick the smaller |w| in order to maximize r"
print sqrt(np.array([x[0],x[1]]).dot(np.array([x[0],x[1]])))

# below is picking 2 negative points +1 positive point
# Step2:solve the equation of (w1,w2,b).dot (x,y,1)=(-1,-1,1)
A=np.array([[3,3,1],[7,2,1],[8,3,1]])
#print " two negative points +1 positive point making matrix A:"
#print A
c=np.array([-1,-1,1])
#print "two negative points +1 positive point make vector c=[-1,-1,1]"
#print c
x=np.linalg.solve(A,c)
print "w1 is :"
print x[0]
print "w2 is:"
print x[1]
print "b is:"
print x[2]
print "margin r=1/|w| is : pick the smaller |w| to maximize r"
print sqrt(np.array([x[0],x[1]]).dot(np.array([x[0],x[1]])))



