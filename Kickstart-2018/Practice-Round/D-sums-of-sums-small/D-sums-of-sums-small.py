# Problem D. Sums of Sums
# URL: https://code.google.com/codejam/contest/4374486/dashboard#s=p3

t = int(input())
for i in range(1, t + 1):
    # input
    (n, q) = (int(s) for s in input().split(" "))
    original = [int(s) for s in input().split(" ")]

    # preprocess
    sum_original = [0]
    for j in range(n):
        sum_original.append(sum_original[j] + original[j])
    new = []
    for j in range(n):
        for k in range(j + 1, n + 1):
            new.append(sum_original[k] - sum_original[j])
    new.sort()
    sum_new = [0]
    for j in range(int(n * (n + 1) / 2)):
        sum_new.append(sum_new[j] + new[j])

    # output
    print("Case #{}:".format(i))
    for j in range(q):
        (start, end) = (int(s) for s in input().split(" "))
        print(sum_new[end] - sum_new[start - 1])
