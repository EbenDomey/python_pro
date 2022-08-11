import numpy as np
from numpy.core.fromnumeric import ndim

arr = np.array((1, 2, 3, 4, 5))
print(arr[::2])
print(arr)
#this was 0-d array
print(np.array(42))
#this is 1-d array
y = np.array([1, 2, 3, 4, 5])
print(y[1:])
print(y[:4])
print(y[1:5:2])
print(y[-2])
#this is 2-d array
t = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print(t[0:2, 1:4])
print(t[1, -1])
u = np.array([[[1, 3, 5, 7], [2, 4, 6, 8]],[[2, 3, 5, 7],[9, 18, 27, 36]]])
print(u[1:5, 1:5, 1:4:2])
print(u[1, 0, 2])
print(y.ndim)
print(t.ndim)
print(u.ndim)
i = np.array([1, 2, 3, 4, 5], ndmin=5)
print(i)
print("This makes it clear that the number of dimensions for this array is ", arr.ndim)
r = np.array([[8, 9, 10, 11, 12], [0, 1, 2, 3, 4]])
print(r[1, 4])