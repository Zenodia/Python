"""SVD is decomposed to Left=U,Sigma,Right=V 
the following SVD=Singular Value Decomposition can be used to calculate
(1) CUR:Moore-Penrose pseudoinverse of matrix A: [1,0,0],[0,2,0],[0,0,0]
week5A quiz answer: [1,0,0],[0,0.5,0],[0,0,0]
(2)Latent Factor: QP decomposition where Q=U, P=Sigma.dot(V) without lambda"""
import numpy as np
from scipy import linalg
#A = np.array([[1,0,0],[0,2,0],[0,0,0]])
A=np.array([[1,1,1,0,0],[3,3,3,0,0],[4,4,4,0,0],[5,5,5,0,0],[0,2,0,4,4],[0,0,0,5,5],[0,1,0,2,2]])
print A
# type in needed # of concept
concept=3
# if we want to project a user q's preference, we simply Vh.dot(q)
q=np.array([[5,0,0,0,0]])


M,N = A.shape
print "shape of matrix A is :"
print
print A.shape
U,s,Vh = linalg.svd(A)
Sig = linalg.diagsvd(s,M,N)
U, Vh = U, Vh
print " U is :"
U_reshape=U[:,:concept]
print -U_reshape
print 
print " diagnal matrix is :"
Sig_reshape=Sig[:concept,:concept]
print Sig_reshape
print
print "V is : "
Vh_reshape=Vh[:concept,:]
print -Vh_reshape
print
print "user q's concept space projection with SVD solution is :"
print -Vh_reshape.dot(q.T)
print
print "check computation is correct, ie see if SVD =A "
print U.dot(Sig.dot(Vh)) #check computation
#create Pseudoinverse
print
print" U transpose is :"
print U.T
#print A.shape
"""get Sigma matrix inverse is simply (1/Sigma) skipping zero diagnal entries"""
def get_invDiagnal(d_matrix):
    m,n=d_matrix.shape
    new_m=np.zeros((m,n))
    for i in range(0,n):
        if d_matrix[i][i]!=0:
            new_m[i][i]=1/(d_matrix[i][i]) # d_matrix[i][i]=Sigma
    return new_m

inv_Sig=get_invDiagnal(Sig)
print
print "the inverse of the diagnal matrix inv_Sig is "
print inv_Sig
#compute Moore-Penrose pseudoinverse
print
print "Moore-Penrose pseudoinverse matrix for input matrix A is : "
print U.T.dot(inv_Sig.dot(Vh))


