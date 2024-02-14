class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cur_sum: int = sum(nums)
        if cur_sum < p:
            return -1
        if 0 == cur_sum % p:
            return 0
        prefix: int = 0
        subs: dict[int, int] = {0: 0}
        out: int = len(nums)
        for index, val in enumerate(nums):
            prefix += val
            sub: int = (prefix - cur_sum) % p
            if sub in subs:
                out = min(out, (index + 1 - subs[sub]))
            subs[prefix % p] = index + 1
        return out if out < len(nums) else -1
