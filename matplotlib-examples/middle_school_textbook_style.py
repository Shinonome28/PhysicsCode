from mpl_toolkits.axisartist.axislines import SubplotZero
from matplotlib.ticker import LinearLocator, MultipleLocator, AutoMinorLocator
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x)

# 配置子图

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

ax.text(1.0, 0.51, "$t$/s", transform=ax.transAxes)
ax.text(0.01, 1.0, "$v$/m/s", transform=ax.transAxes)


def formatter_without_zero(x, pos):
    if abs(x) < 1e-4:
        return ""
    return "{:.2f}".format(x)


ax.xaxis.set_major_locator(MultipleLocator(base=np.pi / 4))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_major_formatter(formatter_without_zero)

ax.yaxis.set_major_locator(LinearLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_formatter(formatter_without_zero)

ax.set_xlim(np.amin(x), np.amax(x))
ax.set_ylim(np.amin(y), np.amax(y))


ax.plot(x, y, c="b")

plt.show()
