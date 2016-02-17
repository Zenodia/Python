# solving system of linear equations with 3 variables
"""
import numpy as np

a = np.array([[1,-1,2], [0,1,-1], [0,0,1]])
b = np.array([5,-1,3])
x = np.linalg.solve(a, b)
print x
"""

# finding eigen values and eigen vectors 
import numpy as np
from numpy.linalg import eigh
# eig is for non-symmetric, eigh is for symmetric(=hamitian matrix)
# given a sample 2x2 matrix
#A=np.array([[1/10,1/10,1/10],[9/20,1/10,1/10],[9/20,8/10,8/10]])
A=np.array([[2.,-1,-1,0,0,0],[-1,3.,0,-1,0,-1],[-1,0,2.,-1,0,0],[0,-1,-1,3.,-1,0],[0,0,0,-1,2.,-1],[0,-1,0,0,-1,2.]])

def get_eigen(M):
#covert to matrix
    M=np.asmatrix(M)
    evals,evecs=np.linalg.eig(A)
    rearrgEvalsEvecs=sorted(zip(evals,evecs.T), key=lambda x:x[0].real, reverse=True)
    # get all sorted eigen values, noted all eigen values are non-negative real numbers
    l=len(rearrgEvalsEvecs)
    all_eVals=[]
    for i in range(0,l):
          all_eVals.append(rearrgEvalsEvecs[i][0])
          print "the %s-th eigen values is: " %i
          print rearrgEvalsEvecs[i][0]
          print " the %s-th eigen vector is :" %i
          print rearrgEvalsEvecs[i][1]
    return rearrgEvalsEvecs, all_eVals

# sort the eignvalues and eigenvectors
# get all eigen values sorted from largest to smallest
all_eValseVecs,eVals=get_eigen(A)

#get the eigen vectors corresponding to the eigenvalue above
#print get_eigen(A)[0][1]
#print " get the eigen vecotr of the 2nd smallest eigen value"
#print get_eigen(A)[4][1]
print " mean value of all the eigen vector values corresponding to 2nd smallest eigen value"
print sum(all_eValseVecs[4][1])/float(6)

# how to import scikit learn
from sklearn import svm
