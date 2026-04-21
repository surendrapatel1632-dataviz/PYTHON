#joining the array using the column_stack
import numpy as np
n1=np.array([2,3,4,5])
n2=np.array([3,4,5,6])
print("itration array1")
for i in n1:
    print(i)
for j in n2:
    print(j)
add=np.column_stack((n1,n2))
print(add)  