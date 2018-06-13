Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> np.array([1,3,6])
array([1, 3, 6])
>>> N=np.array([1,3,6])
>>> N*2
array([ 2,  6, 12])
>>> N**2
array([ 1,  9, 36])
>>> np.log(N)
array([ 0.        ,  1.09861229,  1.79175947])
>>> np.exp(N)
array([   2.71828183,   20.08553692,  403.42879349])
>>> N+N
array([ 2,  6, 12])
>>> N.dot(N)
46
>>> N*N
array([ 1,  9, 36])
>>> (N*N).sum()
46
>>> M=np.array([[1,2],[3,4]])
>>> M[0,0]
1
>>> M[0,1]
2
>>> M[1,1]
4
>>> M[1,0]
3
>>> M=np.matrix([[1,2],[3,4]])
>>> M
matrix([[1, 2],
        [3, 4]])
>>> M.T
matrix([[1, 3],
        [2, 4]])
>>> row=[2,4,6]
>>> sample=map(float, row)
>>> sample
[2.0, 4.0, 6.0]
>>>  
