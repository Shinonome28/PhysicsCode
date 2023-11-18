import numpy as np

x = np.arange(8 * 8 * 8, dtype=np.int32).reshape(8, 8, 8)

# 多维切片
print(x[:, 1:3, 2:4])

# 布尔切片
print(x[x > 100])
print(x[~(x > 100)])
