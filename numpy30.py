#joining the array using the vstack method 
import numpy as np
n1=np.array([5,6,7,8])
n2=np.array([25,30,40,20])
print("itration array1")
for i in n1:
    print(i)
print("itration array2")
for j in n2:
    print(j)
add=np.vstack((n1,n2))
print(add)