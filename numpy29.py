#joining the array using the hstack method 
import numpy as np
n1=np.array([3,4,5,6,7])
n2=np.array([4,5,6,7,9])
print("iterating array1")
for a in n1:
    print(a)
for b in n2:
    print(b)
add=np.hstack((n1,n2))
print(add)