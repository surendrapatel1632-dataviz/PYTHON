#itrate the three dimensional array 
import numpy as np 
n=np.array([[[2,3],[15,20]],[[25,30],[35,40]]])
print("itration")
for a in n:
    print(a)
print("type=",type(n)) 
print("type=",n.dtype)
print("type=",n.ndim)   