class Solution:
    def balancedString(self, s: str) -> int:
        
        cnt = Counter(s)

        n = len(s)
        ans = n
        l = 0

        for r , char in enumerate(s):
            cnt[char] -= 1

            while l < n and all(cnt[i] <= n/4 for i in 'QWER'):
                ans = min(ans, r - l + 1)
                cnt[s[l]] += 1
                l += 1
        return ans
        