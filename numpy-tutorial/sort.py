# 排序函数
# 所有排序函数都有以下三个重要参数：
# axis: 沿着它排序数组的轴，默认按最后一个轴排序
# kind: 默认为'quicksort'（快速排序）
# order: 如果数组包含字段，则是要排序的字段

import numpy as np

np.random.seed(114514)
n_random = (np.random.randint(1, 100) for _ in range(6 * 6))
x = np.fromiter(n_random, dtype=float).reshape(6, 6)
print(x)
print("")

for i in range(2):
    print(np.sort(x, axis=i))
    print("")


for i in range(2):
    print(np.argsort(x, axis=i))
    print("")

print(x[np.lexsort(x)])
print("")

## 其他排序函数
# msort(a)	数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。
# sort_complex(a)	对复数按照先实部后虚部的顺序进行排序。
# partition(a, kth[, axis, kind, order])	指定一个数，对数组进行分区
# argpartition(a, kth[, axis, kind, order])	可以通过关键字 kind 指定算法沿着指定轴对数组进行分区

# 返回非零元素
print(x[np.nonzero(x)])
print("")

# 查找元素
print(x[np.where(x > 5)])
print("")

# 按条件过滤元素
print(np.extract(np.mod(x, 2) == 0, x))
print("")
