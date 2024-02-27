class Solution:
    def spliter(self,  num, right):
        count = num//right
        if num%right:
            count += 1
        num = num//count
        return [count , num]

    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        right = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            if nums[i] > right :
                upCount, right = self.spliter(nums[i], right)
                
                count += upCount-1
            else:
                right = nums[i]
        
        return count
                
                

        print(self.spliter(4,8,3))
        return 0
