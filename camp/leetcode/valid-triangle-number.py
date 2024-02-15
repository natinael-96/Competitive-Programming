class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        ans = 0 
        
        for i in range(n, 1, -1):
            r  = i - 1
            l = 0
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    l += 1
                    
        return ans