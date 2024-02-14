class Solution:
    def bestClosingTime(self, customers: str) -> int:

        n = len(customers)
        preSum = [0]*(n+1)
        
        for i in range(1,n+1):
            if customers[i-1] == "Y":
                preSum[i] += (preSum[i-1] + 1)
            else:
                preSum[i] += preSum[i-1]
        bestT, minPen = 0 , float('inf')
        for i in range(len(preSum)):
            oPen = i - preSum[i]
            cPen = preSum[-1] - preSum[i]
            tPen = oPen + cPen
            if tPen < minPen:
                minPen, bestT = tPen, i
                        
        return bestT











