# Problem C: Sort a scrambled itinerary
# URL: https://code.google.com/codejam/contest/4374486/dashboard#s=p2

t = int(input())
for i in range(1, t + 1):
    # input
    k = int(input())

    # solve
    tickets = {}
    counts = {}
    for j in range(k):
        src = input()
        dest = input()
        tickets[src] = dest
        counts.setdefault(src, 0)
        counts[src] = counts[src] + 1
        counts.setdefault(dest, 0)
        counts[dest] = counts[dest] - 1
        for k in counts:
            if counts[k] == 1:
                start = k
                break

    # output
    src = start
    sorted = ""
    while (src in tickets):
        dest = tickets[src]
        sorted = "{} {}-{}".format(sorted, src, dest)
        src = dest
    print("Case #{}:{}".format(i, sorted))
