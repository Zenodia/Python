import numpy as np
from numpy.linalg import eigh
# eig is for non-symmetric, eigh is for symmetric(=hamitian matrix)
# given a sample 2x2 matrix
#A=np.array([[1/10,1/10,1/10],[9/20,1/10,1/10],[9/20,8/10,8/10]])
# book exercise page 367
"""
A=np.array([[0,1,1,0,0,0,0],[1,0,1,1,0,0,0],[1,1,0,0,0,0,0],[0,1,0,0,1,1,1],[0,0,0,1,0,1,0],[0,0,0,1,1,0,1],[0,0,0,1,0,1,0]])
D=np.array([[2,0,0,0,0,0,0],[0,3,0,0,0,0,0],[0,0,2,0,0,0,0],[0,0,0,4,0,0,0],[0,0,0,0,2,0,0],[0,0,0,0,0,3,0],[0,0,0,0,0,0,2]])
L=D-A
print "the Laplacian matrix is : "
print L
"""
# Quiz week 3A-1
"""
A=np.array([[0,0,1,0,0,1,0,0],[0,0,0,0,1,0,0,1],[1,0,0,1,0,1,0,0],[0,0,1,0,1,0,0,1],[0,1,0,1,0,0,0,1],[1,0,1,0,0,0,1,0],[0,0,0,1,0,1,0,1],[0,1,0,0,1,0,1,0]])
D=np.array([[2,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0],[0,0,3,0,0,0,0,0],[0,0,0,3,0,0,0,0],[0,0,0,0,3,0,0,0],[0,0,0,0,0,3,0,0],[0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,3]])
L=D-A
"""
# Quiz week 3A-2
A=np.array([[0,1,1,0,0,0],[1,0,0,1,0,1],[1,0,0,1,0,0],[0,1,1,0,1,0],[0,0,0,1,0,1],[0,1,0,0,1,0]])
D=np.array([[2,0,0,0,0,0],[0,3,0,0,0,0],[0,0,2,0,0,0],[0,0,0,3,0,0],[0,0,0,0,2,0],[0,0,0,0,0,2]])
L=D-A

print " adjancy matrix A is : "
print A
print "degree matrix D is : "
print D
print " Laplacian matrix L is : "
print L
#print np.linalg.eigvalsh(L)
eigenvalues, eigenvectors=np.linalg.eigh(L)
indexes=np.argsort(eigenvalues)[::-1]
eigval=eigenvalues[indexes]
eigvec=eigenvectors[:,indexes]

print "all eigen values :"
print eigval
#print eigvec
print "2nd smallest eigenvalues is : "
print eigval[-2]
print "the eigen vector correspond to 2nd smallest eigen value is :"
print-eigvec[:,-2]
print "3rd smallest eigenvalues is : "
print eigval[-3]
print "the eigen vector correspond to 3rd smallest eigen value is :"
print -eigvec[:,-3]

l=len(eigvec[:,-2])
ini=0
for i in range(0,l):
    ini+=abs(eigvec[:,-2][i])**2

print "check the sum of square of all the 2nd smallest eigenvectors' entries:"
print ini
print "the SUMSQ of 2nd smallest eigenvectors should be 1=unit eigenvector"
#print float(ini/l)

"""
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
all_eValseVecs,eVals=get_eigen(L)

#get the eigen vectors corresponding to the eigenvalue above
#print get_eigen(A)[0][1]
#print " get the eigen vecotr of the 2nd smallest eigen value"
#print get_eigen(A)[4][1]
print " mean value of all the eigen vector values corresponding to 2nd smallest eigen value"
print sum(all_eValseVecs[4][1])/float(6)
"""
