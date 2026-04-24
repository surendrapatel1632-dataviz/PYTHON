#numpy array diffrence
import numpy as np
n1=np.array([5,10,15,20,25,30,35,40,45,50])
n2=np.array([30,35,50,55,60,65,75.80,95,100])
print("itration array1")
for a in n1:
    print(a)
for a in n2:
    print(a)
diffarr=np.setdiff1d(n1,n2)
print(diffarr)