class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1

        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        count = 0
        occurrences = {}
        for sum in prefix_sum:
            count += occurrences.get(sum - k, 0)
            occurrences[sum] = occurrences.get(sum, 0) + 1

        return count