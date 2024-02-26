class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def helper(i, path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for j in range(len(nums)):
                if nums[j] not in path:
                    path.append(nums[j])
                    helper(j,path)
                    path.pop()
        helper(0,[])
        return ans