# in array using the split method
import numpy as np
n=np.array([10,20,30,40,50,60])
print("iterating the array")
for i in n:
    print(i)
new_array=np.array_split(n,3)
for j in new_array:
    print("\nsplit array",j)
