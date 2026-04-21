import numpy as np
n1=np.array([5,10,15,25])
n2=np.array([25,30,40])
print("itrrating array1")
for a in n1:
    print(a)
print("itrrating array2")
for b in n2:
    print(b)
add=np.concatenate((n1,n2))
print("joining",add)        