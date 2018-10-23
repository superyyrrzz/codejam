# Problem D: Bathroom Stalls
# URL: https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard/0000000000000652
# This version meets TIME_LIMIT_EXCEEDED in test set 2

import heapq
import math


def ChooseBathroom(n, k):
    max_heap = [-n]
    count_dict = {n : 1}
    p = 0
    while True:
        max_spaces = -heapq.heappop(max_heap)
        max = math.ceil((max_spaces - 1) / 2)
        min = math.floor((max_spaces - 1) / 2)
        p += count_dict[n]
        if p >= k:
            return (max, min)
        heapq.heappush(max_heap, -max)
        count_dict[max] = count_dict.setdefault(max, 0) + count_dict[n]
        heapq.heappush(max_heap, -min)
        count_dict[min] = count_dict.setdefault(min, 0) + count_dict[n]


t = int(input())
for i in range(1, t + 1):
    [n, k] = [int(s) for s in input().split()]
    (max, min) = ChooseBathroom(n, k)
    print("Case #{}: {} {}".format(i, max, min))
