import numpy as np
tam = np.array([1, 2, 3, 4, 5, 6, 7, 8])
tr = tam.reshape(2, 2, -1)
print(tr)
print(tr.base)
yam = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
ur = yam.reshape(-1)
print(yam)
print(ur)
