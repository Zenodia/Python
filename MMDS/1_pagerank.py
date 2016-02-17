# wk1 homework, pagerank calculation with taxiation

# construct matrix A using wk last video as example
import numpy as np
# exampe matrix A
A=np.array([[1./2, 1./2,0],[1./2,0,0],[0,1./2,1]])

A_quiz3=np.array([[0,0,1],[1./2,0,0],[1./2,1.,0]]) # for quiz 3 wk1

#initial r as 1st iteration
r=np.array([[1./3,1./3,1./3]])

# make a function that remake a matrix with taxiation included
""" below is so that we can see what the new matrix adding (1-b)/n will look like
def add_tax(M,beta):
    #beta is a number usually between 0 and 1 as tax
    l=len(M)
    num=1.0/l
    Ad=num*(np.ones(l))
    print Ad
    #M=beta*M+(1-beta)*Ad
    return M,Ad
"""
# perform single step in pagerank computation
def step(M,r,b):
    n=len(M)
    num=(1-b)*(1./n)
    Ad=num*(np.ones(n))
    r1=b*(np.dot(M,r.T))
    return r1.T+Ad.T
#print step(A,r,0.8)

# power iteration function
def pagerank(M,s, tolerance=0.001):
    # the pagerank is consider converged when the threshold of tolerance is met
    n=len(M)
    r=np.ones(n)*(1./n)
    r=np.ones(n) # for quiz3
    iteration=1
    change=2
    while change>tolerance:
        new_r=step(M,r,s)
        change=np.sum(np.abs(r-new_r))
        print " tolerance is now : %s" %change
        r=new_r
        iteration+=1
        print "%s_th iteration, r now is %s)" %(iteration-1, r)
    return r
#print pagerank(A,0.8,tolerance=0.001)
print pagerank(A_quiz3,1,0.001) # for quiz3 wk1
