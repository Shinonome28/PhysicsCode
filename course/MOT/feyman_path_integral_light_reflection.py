"""
模拟光的反射的费曼路径积分。相当不准确，只能看一个趋势。
正确的方法是做一个积分，但要带一个复杂的积分元，不然积分收敛。
"""
import matplotlib.pyplot as plt
from cmath import *

X = -5.0
Y = 3.0
K = 1000


def phase_factor(x: complex):
    return exp(
        complex(0, K * (sqrt((x - X) ** 2 + Y**2) + sqrt((x + X) ** 2 + Y**2)))
    )


if __name__ == "__main__":
    N = 1000
    n = (1.0 - X) / N
    r = 0 + 0j
    p = []
    for i in range(N):
        r += phase_factor(X + n * i)
        p.append((X + n * i, abs(r)))

    x_points = [i[0] for i in p]
    y_points = [i[1] for i in p]
    plt.plot(x_points, y_points)
    plt.show()
