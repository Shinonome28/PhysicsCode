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


# 形状操作

## reshape

x = np.arange(24).reshape(2, 3, 4)
inspect_array(x)

## 展平

x = x.flatten()
inspect_array(x)

# 翻转操作

## transpose

x = np.arange(12).reshape(3, 4)
inspect_array(x.T)

## rollaxis

x = np.arange(2 * 3 * 4).reshape(2, 3, 4)
inspect_array(x)
inspect_array(np.rollaxis(x, 2, 0), label="rollaxis")
inspect_array(np.swapaxes(x, 0, 1), label="swap axis")
