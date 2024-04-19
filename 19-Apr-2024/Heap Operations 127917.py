# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq

heap = []
heapq.heapify(heap)
ans = []

for i in range(int(input())):
    inp = input().split()
    op = inp[0]
    if len(inp) == 2:
        nm = int(inp[1])
    
    if op == 'insert':
        heapq.heappush(heap, nm)
        ans.append((op, nm))
        
    elif op == 'getMin':
        while heap and heap[0] < nm:
            heapq.heappop(heap)
            ans.append(('removeMin', ''))
            
        if not heap or heap[0] > nm:
            heapq.heappush(heap, nm)
            ans.append(('insert', nm))
        
        ans.append((op, nm))
    else:
        if not heap:
            ans.append(('insert', 0))
        else:
            heapq.heappop(heap)
        ans.append((op, ''))

print(len(ans))
for i in ans:
    print(*i)
