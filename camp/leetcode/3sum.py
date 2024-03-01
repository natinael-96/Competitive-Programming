class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        if n < 3:
            return res
        
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            elif (i > 0) and (nums[i] == nums[i-1]):
                continue 
            
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return res
