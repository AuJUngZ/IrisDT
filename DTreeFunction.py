import math


def entropy(x, y, z):
    sum_row = x + y + z
    if x == 0 or y == 0 or z == 0:
        return 0
    else:
        return (-x / sum_row) * math.log2(x / sum_row) - (y / sum_row) * math.log2(y / sum_row) - (
                z / sum_row) * math.log2(z / sum_row)


def inforD(m, n):
    """
    m is array of class in each attb group by domain
    n is array of entropy
    """
    c = len(m)
    # print(" size m is ",c)
    out = 0
    i = 0
    for i in range(c):
        # print("m[i] is", m[i])
        # print("sum(m) is ", sum(m))
        out += (m[i] / sum(m)) * n[i]
    # print("out is ",out)
    return out
