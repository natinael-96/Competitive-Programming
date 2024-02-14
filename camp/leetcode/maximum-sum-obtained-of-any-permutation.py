class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse =True)
        mod =10**9 + 7
        ordr = [0]*(len(nums) +1)
        for l,r in requests:
            ordr[l] += 1
            ordr[r+1] -= 1
        for i in range(1,len(ordr)):
            ordr[i] += ordr[i-1]
        ordr.sort(reverse=True)

        for i in range(len(nums)):
            ordr[i] *= nums[i]
        
        
        
        
        return sum(ordr)%mod