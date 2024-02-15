class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)
        
        for i in range(n):
            for j in range(n - i - 1):
                # Compare nums[j] and nums[j + 1] as strings
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
        largest_num = ''.join(nums)
    
        return str(int(largest_num)) if largest_num != "0" else largest_num