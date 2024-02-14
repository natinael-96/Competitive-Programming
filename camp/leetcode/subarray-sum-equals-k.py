class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = defaultdict(int)
        preS = 0
        count = 0
        for i in range(len(nums)):
            preS = nums[i] + preS
            if preS - k in sums:
                count += sums[preS - k]
            if preS == k:
                count += 1
            sums[preS] += 1
        return count

                

                
            
