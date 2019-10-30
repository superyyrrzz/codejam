# Problem B: Senate Evacuation
# URL: https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/00000000000004c0


def evacuate(n, ps):
    arr1 = []
    arr2 = []
    char = "A"
    res = []

    for i in range(n):
        if len(arr1) > len(arr2):
            current = arr2
        else:
            current = arr1
        for _ in range(ps[i]):
            current.append(char)
        char = chr(ord(char) + 1)

    while (len(arr1) > 0 and len(arr2) > 0):
        if len(arr1) > len(arr2):
            long = arr1
            short = arr2
        elif len(arr1) < len(arr2):
            long = arr2
            short = arr1
        else:
            res.append(arr1.pop() + arr2.pop())
            continue
        if (len(long) - len(short) >= 2):
            res.append(long.pop() + long.pop())
        else:
            res.append(long.pop())

    return res


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ps = [int(p) for p in input().split(" ")]
    res = evacuate(n, ps)
    print("Case #{}: ".format(i) + " ".join(res))
