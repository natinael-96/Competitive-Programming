class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        distinct = len(set(nums))
        l, r, count =0, 0 ,0
        counter = Counter()

        while r < len(nums):
            counter[nums[r]] += 1

            while len(counter) == distinct:
                counter [nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
                count += (len(nums)) - r
            r += 1
        return count

