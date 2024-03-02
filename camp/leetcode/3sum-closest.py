class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest_sum = math.inf
        for frst, val in enumerate(nums[:-2]):
            mid, last = frst + 1, len(nums) - 1
            while mid < last:
                current_sum = val + nums[mid] + nums[last]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum > target:
                    last -= 1
                if current_sum < target:
                    mid += 1
                if current_sum == target:
                    break

        return closest_sum