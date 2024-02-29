class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # n true false questions T/F
        # maximize consecutive que with same ans
        # answerKey[i] , k - max opp
        # opp - replace t with f

        scoreCount = {"T": 0, "F":0}

        maxOut = 0
        l = 0
        for r in range(len(answerKey)):
            scoreCount[answerKey[r]] += 1

            if scoreCount['T'] > k and scoreCount['F'] > k:
                scoreCount[answerKey[l]] -= 1
                l += 1
            
            maxOut = max(maxOut, r - l + 1)
    
        return maxOut

            