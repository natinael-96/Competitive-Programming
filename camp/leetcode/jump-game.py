class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1

        reach = 0
        for i, jump in enumerate(nums):
            if reach < i: 
                return False
            
            reach = max(reach, jump+i)
            if reach >= last: 
                return True
