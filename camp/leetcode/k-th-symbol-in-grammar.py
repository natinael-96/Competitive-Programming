class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n,k):
            tot = 2 ** (n - 1)

            if n > 2:
                if k <= tot//2:
                    return helper(n-1, k)
                else:
                    if k > tot//2 and k <= tot*3/4:
                        return helper(n-1, k-tot//4)
                    else:
                        return helper(n-1, k-(3*tot//4))
            elif n == 2:
                return 0 if k == 1 else 1
            else: 
                return 0
        return helper(n,k)
            