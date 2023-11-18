import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(
    x, y, marker="*", ms=6, mfc="r", mec="r"
)  # ms = marker size, mfc = marker face color, mec = marker edge color
# 设定颜色可以使用16进制RGB颜色代码，例如 #4CAF50
plt.show()
