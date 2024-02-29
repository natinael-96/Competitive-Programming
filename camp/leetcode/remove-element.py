class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = 0
        for indx in range(len(nums)):
            if nums[indx] != val:
                nums[num] = nums[indx]
                num += 1
        return num