import math
import matplotlib.pyplot as plt

CONSTANTS = {
    "a": 10.0,
    "b": 8.0 / 3,
    "w": 7.62,
    "dt": 0.001,
    "r0": 26,
    "r1": 10,
    "iterationTimes": 200000,
    "displayAfter": 5000 * 10,
    "displayEnd": 5000 * 15,
}

ARGS0 = (1.0, 1.0, 1.0)
ARGS1 = (1.1, 1.0, 1.0)


def calcultion(args, label=None):
    result = []
    x, y, z = args
    t = 0.0
    for i in range(CONSTANTS["iterationTimes"]):
        xinc1 = equationX(x, y, z, t) * CONSTANTS["dt"]
        yinc1 = equationY(x, y, z, t) * CONSTANTS["dt"]
        zinc1 = equationZ(x, y, z, t) * CONSTANTS["dt"]

        xinc2 = (
            equationX(x + 0.5 * xinc1, y + 0.5 * yinc1, z + 0.5 * zinc1, t)
            * CONSTANTS["dt"]
        )
        yinc2 = (
            equationY(x + 0.5 * xinc1, y + 0.5 * yinc1, z + 0.5 * zinc1, t)
            * CONSTANTS["dt"]
        )
        zinc2 = (
            equationZ(x + 0.5 * xinc1, y + 0.5 * yinc1, z + 0.5 * zinc1, t)
            * CONSTANTS["dt"]
        )

        xinc3 = (
            equationX(x + 0.5 * xinc2, y + 0.5 * yinc2, z + 0.5 * zinc2, t)
            * CONSTANTS["dt"]
        )
        yinc3 = (
            equationY(x + 0.5 * xinc2, y + 0.5 * yinc2, z + 0.5 * zinc2, t)
            * CONSTANTS["dt"]
        )
        zinc3 = (
            equationZ(x + 0.5 * xinc2, y + 0.5 * yinc2, z + 0.5 * zinc2, t)
            * CONSTANTS["dt"]
        )

        xinc4 = equationX(x + xinc3, y + yinc3, z + zinc3, t) * CONSTANTS["dt"]
        yinc4 = equationY(x + xinc3, y + yinc3, z + zinc3, t) * CONSTANTS["dt"]
        zinc4 = equationZ(x + xinc3, y + yinc3, z + zinc3, t) * CONSTANTS["dt"]

        x += (xinc1 + 2 * xinc2 + 2 * xinc3 + xinc4) / 6
        y += (yinc1 + 2 * yinc2 + 2 * yinc3 + yinc4) / 6
        z += (zinc1 + 2 * zinc2 + 2 * zinc3 + zinc4) / 6
        t += CONSTANTS["dt"]

        if i >= CONSTANTS["displayAfter"]:
            result.append((x, y, z, t))

        if i >= CONSTANTS["displayEnd"]:
            break

    # print(result)
    xPoints = [t[0] for t in result]
    yPoints = [t[1] for t in result]
    zPoints = [t[2] for t in result]
    tPoints = [t[3] for t in result]

    plt.clf()
    plt.axis("off")
    plt.plot(tPoints, xPoints, color="black")
    if label is None:
        plt.show(block=True)
    else:
        plt.savefig(
            "output/{0}_{1}_{2}.png".format(
                label,
                CONSTANTS["displayAfter"],
                CONSTANTS["displayEnd"],
            )
        )


def equationX(x, y, z, t):
    return -CONSTANTS["a"] * x + CONSTANTS["a"] * y


def equationY(x, y, z, t):
    r = CONSTANTS["r0"] + CONSTANTS["r1"] * math.cos(CONSTANTS["w"] * t)
    return -x * z + r * x - y


def equationZ(x, y, z, t):
    return -CONSTANTS["b"] * z + x * y


if __name__ == "__main__":
    calcultion(ARGS0, label="x0_no_sensitive")
    calcultion(ARGS1, label="x1_no_sensitive")
