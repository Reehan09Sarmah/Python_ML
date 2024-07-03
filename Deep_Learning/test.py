import numpy as np

a = np.array([[2, 1], [1, 3]])
print(np.dot(a, a))

b = np.random.randn(3, 3)
c = np.random.randn(3, 1)
print(b)
print(c)
d = b * c
print(d)

x = np.array([[[1],[2]], [[3], [4]]])
print(x.shape)
