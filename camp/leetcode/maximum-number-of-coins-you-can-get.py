class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
    
        n = len(piles) // 3  
        coins = 0
        
        for i in range(n, len(piles), 2):
            coins += piles[i]
        
        return coins