import numpy as np
n1 = np.random.randint(1,100,5)
print(n1)

n1 = np.array([[1,2,3],[4,5,6]])
print(n1)
n1.shape = (3,2)
print(n1)

n3 = np.array([5,10,15,20,25])
n4 = np.array([30,35,40,45,50])
print(np.vstack((n3,n4)))
print(np.hstack((n3,n4)))
print(np.column_stack((n3,n4)))
ny=np.zeros((3,2))
print(ny)