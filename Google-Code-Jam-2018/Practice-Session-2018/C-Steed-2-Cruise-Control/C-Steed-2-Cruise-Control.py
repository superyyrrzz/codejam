# Problem C: Steed 2: Cruise Control
# URL: https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000524


def ChooseSpeed(d, n, k, s):
    tmax = 0
    for i in range(n):
        t = (d - k[i]) / s[i]
        tmax = max(t, tmax)
    return d / tmax


t = int(input())
for i in range(1, t + 1):
    [d, n] = [int(c) for c in input().split()]
    k = []
    s = []
    for j in range(n):
        [kt, st] = [int(c) for c in input().split()]
        k.append(kt)
        s.append(st)
    speed = ChooseSpeed(d, n, k, s)
    print("Case #{}: ".format(i) + str(round(speed, 6)))
