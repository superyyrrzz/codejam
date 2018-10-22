# Problem D: Bathroom Stalls
# URL: https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard/0000000000000652
# This version meets TIME_LIMIT_EXCEEDED in test set 2

import heapq
import math


def ChooseBathroom(n, k):
    max_heap = [-n]
    for _ in range(k):
        max_spaces = -heapq.heappop(max_heap)
        max = math.ceil((max_spaces - 1) / 2)
        min = math.floor((max_spaces - 1) / 2)
        heapq.heappush(max_heap, -max)
        heapq.heappush(max_heap, -min)
    return (max, min)


t = int(input())
for i in range(1, t + 1):
    [n, k] = [int(s) for s in input().split()]
    (max, min) = ChooseBathroom(n, k)
    print("Case #{}: {} {}".format(i, max, min))
