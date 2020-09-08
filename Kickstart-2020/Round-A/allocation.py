# URL: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56#problem


def allocation(n, b, prices):
    prices.sort()
    remaining = b
    result = 0
    for price in prices:
        if price <= remaining:
            remaining -= price
            result += 1
        else:
            return result
    return result


t = int(input())
for i in range(1, t + 1):
    # input
    (n, b) = [int(s) for s in input().split(" ")]
    prices = [int(s) for s in input().split(" ")]

    # solve
    result = allocation(n, b, prices)

    # output
    print("Case #{}: {}".format(i, result))
