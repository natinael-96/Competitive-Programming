class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def helper(i,path):
            if sorted(path) not in ans:
                ans.append(path[:])

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1] :
                    continue
                path.append(nums[j])
                helper(j+1, path)
                path.pop()
        helper(0,[])
        return list(ans)

        