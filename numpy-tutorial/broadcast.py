import numpy as np

a = np.arange(3 * 3).reshape(3, 3)
b = np.arange(3)
print(a + b)

# 广播迭代
for x, y in np.nditer([a, b]):
    print(x, y)
