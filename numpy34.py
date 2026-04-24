# opretion for intersection method
import numpy as np
n1=np.array([10,20,30,40,50])
n2=np.array([60,70,80,90,100])
print("itretting array1")
for a in n1:
    print(a)
print("itretting array2")
for a in n2:
    print(a)
con=np.intersect1d(n1,n2)
print("common element",con)        