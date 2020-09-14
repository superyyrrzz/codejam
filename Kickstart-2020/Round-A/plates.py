# URL: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb


def plates(v, n, k, p):
    """
    v : int[][]
        plates values, v[i][j] means the value of the (j + 1)th plate in the (i + 1)th stack
    n : int
        stacks of plates
    k : int
        plates in each stack
    p : int
        plates to take
    """

    # agg_v[i][j] is the value if take j plates in the (i + 1)th stack
    agg_v = []
    for i in range(n):
        agg_v_of_stack_i = [0] * (k + 1)
        for j in range(1, k + 1):
            agg_v_of_stack_i[j] = agg_v_of_stack_i[j - 1] + v[i][j - 1]
        agg_v.append(agg_v_of_stack_i)

    # v_max[i][j] is the max value if take (j) plates from last (i) stacks
    v_max = [[0] * (p + 1)]  # the first row is all 0s
    for i in range(1, n + 1):  #
        v_max_of_i = [0] * (p + 1)
        for j in range(1, p + 1):  # start from 1, as the first column is all 0s
            for t in range(0, k + 1):  # assume we take (t) plates from the (n - i + 1)'s stack
                if j - t >= 0:
                    v_max_of_i[j] = max(
                        v_max_of_i[j],
                        agg_v[n - i][t] + v_max[i - 1][j - t])
        v_max.append(v_max_of_i)

    return v_max[n][p]


t = int(input())
for i in range(1, t + 1):
    # input
    (n, k, p) = [int(s) for s in input().split(" ")]
    v = []
    for j in range(0, n):
        values = [int(s) for s in input().split(" ")]
        v.append(values)

    # solve
    result = plates(v, n, k, p)

    # output
    print("Case #{}: {}".format(i, result))
