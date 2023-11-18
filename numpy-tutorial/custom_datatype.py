import numpy as np

dt = np.dtype([("age", np.int32), ("id", np.int32)])
a = np.array([(12, 11001), (13, 20002)], dtype=dt, ndmin=2)
print(dt)
print(a)
