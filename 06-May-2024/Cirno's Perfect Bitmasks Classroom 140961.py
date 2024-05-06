# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    x = int(input())
    y = x & (-x)
    while  (not (y ^ x) or not(y & x)):
        y += 1
    print(y)
