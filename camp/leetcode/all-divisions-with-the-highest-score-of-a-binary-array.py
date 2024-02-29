class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        cnt_1 = 0
        for num in nums:
            if num == 1: cnt_1 += 1
        
        cnt_0, maxDiv = 0, cnt_1
        d = defaultdict(list)
        d[cnt_1].append(0)
        for i, num in enumerate(nums):
            cnt_0 += int(num == 0)
            cnt_1 -= int(num == 1)
            d[cnt_0 + cnt_1].append(i + 1)
            maxDiv = max(maxDiv, cnt_0 + cnt_1)
        return d[maxDiv]