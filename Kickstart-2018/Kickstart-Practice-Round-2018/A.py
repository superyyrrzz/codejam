# Problem A: GBus count
# URL: https://code.google.com/codejam/contest/4374486/dashboard#s=p0


def count_less(stops, target):
    left = 0
    right = len(stops) - 1
    if stops[right] < target:
        return right + 1
    elif target <= stops[left]:
        return 0
    while True:
        i = int((left + right) / 2)
        if (stops[i] < target and stops[i + 1] >= target):
            return i + 1
        if (stops[i] >= target):
            right = i
        elif (stops[i + 1] < target):
            left = i


t = int(input())
for i in range(1, t + 1):
    # input
    n = int(input())
    covers = [int(s) for s in input().split(" ")[:-1]]
    alist, blist = covers[::2], covers[1::2]
    p = int(input())
    clist = []
    for j in range(p):
        clist.append(int(input()))
    input()

    # solve
    alist.sort()
    blist.sort()
    res = []
    for j in range(p):
        res.append(count_less(
            alist, clist[j] + 1) - count_less(blist, clist[j]))

    # output
    print("Case #{}: ".format(i) + " ".join([str(r) for r in res]))
