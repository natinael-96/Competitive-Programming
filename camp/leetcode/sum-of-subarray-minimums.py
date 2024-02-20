class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        prev = [-1]*n
        nxt = [n]*n

        # prev
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        
        stack = []

        # nxt
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                nxt[i] = stack[-1]
            stack.append(i)
        
        ans = [(i - prev[i]) * (nxt[i]  - i)* arr[i] for i in range(n)]
        MOD = 10**9 + 7
        return sum(ans) % MOD
