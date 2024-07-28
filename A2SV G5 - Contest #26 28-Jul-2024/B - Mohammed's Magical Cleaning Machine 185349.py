# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = 0
    for i in arr[:-1]:
        if i or mx > i:
            mx += i + int(i == 0)
    print(mx)