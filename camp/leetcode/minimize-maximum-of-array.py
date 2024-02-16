class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_val = cur_sum = 0

        for ind, num in enumerate(nums):            
            cur_sum += num

            if num > max_val:
                mid_float = cur_sum / (ind + 1)
                mid_int = int(-1 * mid_float // 1 * -1)
                max_val = max([max_val, mid_int])

        return max_val