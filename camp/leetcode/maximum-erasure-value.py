class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int: 

        
        ans = cur = start = 0   
        d = {}          

        for i,j in enumerate(nums):
            if i > 0: nums[i] += nums[i-1]      
            cur += j                
            if j in d and d[j] >= start:  
                ind = d[j] 
                cur = cur - (nums[ind] - nums[start-1] if start != 0 else nums[ind])  
                start = ind + 1     
            d[j] = i  
            ans = max(ans,cur)

        return ans