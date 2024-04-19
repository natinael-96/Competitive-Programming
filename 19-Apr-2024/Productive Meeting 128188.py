# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr = [(-i, ind + 1) for ind, i in enumerate(arr) if i > 0]
    heapq.heapify(arr)
    ans = []

    if len(arr) == 1:
        print(0)
        continue

    while len(arr) > 1:
        x, y = heapq.heappop(arr), heapq.heappop(arr)
        ans.append((x[1], y[1]))

        if -x[0] > 1:
            heapq.heappush(arr, (x[0] + 1, x[1]))
        if -y[0] > 1:
            heapq.heappush(arr, (y[0] + 1, y[1]))

    print(len(ans))
    for i in ans:
        print(*i)
