import numpy as np

# 以下函数，一个很重要的参数的是axis，即在那个轴上统计。被统计的轴将变为长度为1的一维数组。
# 还有一个很重要的参数是where，只考虑符合条件的元素

## 最大最小值

x = np.arange(9).reshape(3, 3)

print(x)

print(np.amax(x))
for i in range(2):
    print(np.amax(x, axis=i))
print("")
print(np.amin(x))
for i in range(2):
    print(np.amin(x, axis=i))
print("")

## 峰峰值
print(np.ptp(x))
for i in range(2):
    print(np.ptp(x, axis=i))
print("")

## 百分位数
print(np.percentile(x, 50))
for i in range(2):
    print(np.percentile(x, 50, axis=i))
print("")

## 中位数
print(np.median(x))
for i in range(2):
    print(np.median(x, axis=i))
print("")

## 平均值
print(np.mean(x))
for i in range(2):
    print(np.mean(x, axis=i))
print("")

## 标准差
print(np.std(x))
for i in range(2):
    print(np.std(x, axis=i))
print("")

## 方差
print(np.var(x))
for i in range(2):
    print(np.var(x, axis=i))
print("")
