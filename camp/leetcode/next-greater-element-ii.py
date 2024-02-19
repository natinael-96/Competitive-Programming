class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [-1]*n

        stack = []
        for i in range(2*len(nums)):

            idx = i % len(nums)

            while stack and nums[stack[-1]] < nums[idx]:
                nm = stack.pop()
                out[nm] = nums[idx]
                         
            

            stack.append(idx)
        return out


