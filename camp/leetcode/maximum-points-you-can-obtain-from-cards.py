class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        for i in range(1,len(cardPoints)):
            cardPoints[i] += cardPoints[i-1]
        
        card = [0]+cardPoints   
        winSize = len(card) - k 
        maxC = 0
        for r in range(winSize,len(card)+1):
            l = r - winSize
            maxC = max(maxC, card[-1] - card[r-1] + card[l] - card[0])
        return maxC