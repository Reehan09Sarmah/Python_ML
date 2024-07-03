import time
import numpy as np

np.random.seed(1)
a = np.random.rand(1000000)
b = np.random.rand(1000000)


tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(f"np.dot(a, b) = {c:.4f}")
print(f"vectorized version duration: {1000 * (toc-tic): .4f} ms")