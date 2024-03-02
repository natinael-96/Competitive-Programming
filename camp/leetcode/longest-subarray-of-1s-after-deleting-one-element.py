class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        l = 0
        zero = 0
        ones = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1
                while zero > 1:
                    if nums[l] == 0:
                        zero -= 1
                    else:
                        ones -= 1
                    l += 1
            else:
                ones += 1

            answer = max(answer, ones)

        return answer if zero == 1 else answer - 1
