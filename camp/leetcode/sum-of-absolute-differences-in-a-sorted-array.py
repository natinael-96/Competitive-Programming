class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = [0]*len(nums) , [sum(nums)]*len(nums)
        pre[0] = nums[0]

        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
            suf[i] = suf[i-1]- nums[i-1]

        out = [0]*len(nums)

        for i in range(n):
            pr = nums[i]*(i) - pre[i]
            su = suf[i] - (n-i-1)*nums[i]
            out[i] = (pr+su)
        return out