class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sumFreq = defaultdict(int)
        count = 0
        Sum = 0

        for i in nums:
            Sum += i

            if Sum % k == 0:
                count += 1
            
            difDiv = (Sum - k)%k

            if difDiv in sumFreq:
                count += sumFreq[difDiv]
            
            sumFreq[Sum % k] += 1
            
        return count