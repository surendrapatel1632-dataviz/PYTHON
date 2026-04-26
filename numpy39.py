# add the individual array values using the axis parameter
import numpy as np
n1=np.array([15,20,25])
n2=np.array([65,75,30])
indarray=np.sum([n1,n2],axis=1)
print(indarray)