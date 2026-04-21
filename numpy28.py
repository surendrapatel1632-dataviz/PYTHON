#joining the array using the stack method 
import numpy as np
n1=np.array([12,13,14,15])
n2=np.array([23,24,25,26])
print("iteration")
for a in n1:
    print(a)
for b in n2:
    print(b)
add=np.stack((n1,n2),axis=1)
print("after joining",add)        