import numpy as np
import time
import sys
size =1000000
s1=range(size)
s2=range(size)

d1=np.arange(size)
d2=np.arange(size)
start=time.time()

result=[(x+y) for x,y in zip(s1,s2)]
print result
print ((time.time()-start)*1000)
result=d1+d2
print ((time.time()-start)*1000)
print result
