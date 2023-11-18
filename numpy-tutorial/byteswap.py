# 交换字节序
# 对于网络传输有用

import numpy as np


def swap_bytes(s):
    b = s.encode("utf-16")
    A = np.frombuffer(b, dtype=np.uint16)
    print(s)
    print(list(map(hex, A)))
    A = A.byteswap()
    print(A.tobytes().decode("utf-16"))
    print(list(map(hex, A)))


swap_bytes("你好世界")
