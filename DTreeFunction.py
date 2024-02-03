import math

def entropy2(n):
    sum_row = sum(n)
    #     if member of n is 0
    if 0 in n:
        return 0
    else:
        return sum([(-x / sum_row) * math.log2(x / sum_row) for x in n])


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
