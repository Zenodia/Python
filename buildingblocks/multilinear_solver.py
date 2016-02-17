import numpy as np
from scipy import linalg
# solve multilinear equation for 3 variables 
# assuming matrix A with 3 variables w1, w2 and b
# to solve Support Vector Machine problem to find the decision line/boundary
# pick 3 points as support vectors: two choices
#(1) 2 positives + 1 negatives:x1(5,4) +1 , x2(8,3) +1 and x3(7,2) -1
#(2) 2 negatives + 1 positive :x3(7,2) -1,x4(3,3) -1 ,x2(8,3) +1
# make SURE you pick the (1)negative point which is cloest
# to the line went through the two positive points x1(5,4) +1 and x2(8,3) +1 for (1)
# or for (2) then pick the (2) positive point which is cloese to the line
# went through the two negative points x4(3,3) -1 and x3(7,2) -1

# finding the cloese negative points for equation (1) : 2 positive + 1 negative
# the line went through the line that went through 2 positive points is
# in the form of y=ax +b
x1=np.array([5,4]) # positive 1
x2=np.array([8,3]) # positive 1
x3=np.array([7,2]) # negative -1
x4=np.array([3,3]) # negative -1
# creating the positive line which goes through 2 positive points x1 and x2 in the form y=ax+c
C=np.array([[x1[0],1],[x2[0],1]])
c=np.array([x1[1],x2[1]])
posline=np.linalg.solve(C,c)

print " the line the went through the two positive point with the form y=%sx+%s :" % (posline[0],posline[1])
                                                                                      
def pick_closer(point1,point2):
    point1dist=posline[0]*point1[0]-point1[1]+posline[1]
    point2dist=posline[0]*point2[0]-point2[1]+posline[1]
    print " %s distance is :%s" %(point1,point1dist)
    print " %s distance is :%s "%(point2,point2dist)
    if point1dist<point2dist:
        print "choose point : %s" %point1
        return point1
    else:
        print " choose point : %s" %point2
        return point2

closerpoint=pick_closer(x3,x4)

neg_add=np.append(closerpoint,1)
# use the choosen point to solve the multilinear  equation given the form
# w1*x+w2*y+b=1 for positive points w1*x+w2*y+b=-1
A=np.array([[5,4,1],[8,3,1],neg_add])
b=np.array([1,1,-1])
x=np.linalg.solve(A,b)
print "w1 is :"
print x[0]
print "w2 is :"
print x[1]
print " b is : "
print x[2]


