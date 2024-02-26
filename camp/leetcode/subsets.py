class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subs = []

        def backTrack(ind, path):
            subs.append(path[:])
            
            for i in range(ind,len(nums)):
                path.append(nums[i])
                backTrack(i+1,path)
                path.pop()
        backTrack(0,[])
        return subs