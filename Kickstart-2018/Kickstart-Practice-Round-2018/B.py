# Problem B: Googol String
# URL: https://code.google.com/codejam/contest/4374486/dashboard#s=p1


def kth_char(k):
    if k == 1:
        return 0

    # find max(m): 2 ** m <= k
    m = 0
    t = k >> 1
    while t > 0:
        t = t >> 1
        m = m + 1
    mfull = 1 << m

    if k == mfull:
        return 0
    else:
        return 1 - kth_char((mfull << 1) - k)


t = int(input())
for i in range(1, t + 1):
    # input
    k = int(input())

    # solve
    res = kth_char(k)

    # output
    print("Case #{}: {}".format(i, res))
