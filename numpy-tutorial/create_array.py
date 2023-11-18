import numpy as np


def inspect_array(a, label=None):
    if label is not None:
        print(label)
    print(a)
    print(
        "size: {}, shape: {}, dtype: {} totalsize: {} Byte".format(
            a.size, a.shape, a.dtype, a.itemsize * a.size
        )
    )


x = np.empty([3, 4], dtype=np.int32)
inspect_array(x, "empty")

x = np.zeros([3, 4], dtype=np.int32)
inspect_array(x, "zeros")

x = np.ones([3, 4], dtype=np.int32)
inspect_array(x, "ones")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.ones_like(arr)
inspect_array(x, "ones_like")

s = b"Hello World"
x = np.frombuffer(s, dtype="S1")
inspect_array(x, "frombuffer")

x = np.fromiter(range(100), dtype=float)
inspect_array(x)

x = np.arange(5, dtype=float)
inspect_array(x)

x = np.linspace(10, 20, 5)
inspect_array(x)

x = np.logspace(1.0, 2.0, num=10)
inspect_array(x)
