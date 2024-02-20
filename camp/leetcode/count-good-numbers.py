class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD =10**9 + 7
        def powCal(base, powr):
            MOD =10**9 + 7
            if powr < 1:
                return 1
            if powr %2 == 0:
                return powCal((base*base)%MOD , powr//2)
            else:
                return base * powCal((base*base)%MOD , (powr - 1)//2)
        # 5^((n+1)/2) by 4^(n/2)
        return (powCal(5, (n+1)//2) * powCal(4, n//2)) % MOD