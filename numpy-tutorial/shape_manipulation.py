import numpy as np

a = np.arange(24)
print("{} {}".format(a.size, a.shape))


a = a.reshape(2, 3, 4)
print("{} {}".format(a.size, a.shape))

print(a.flags)
