class NumArray:

    def __init__(self, nums: List[int]):
        
        self.Sum = [0]*(len(nums)+1)

        for i in range(1,len(nums)+1):
            self.Sum[i] = self.Sum[i -1] + nums[i-1]
            

    def sumRange(self, left: int, right: int) -> int:

        return self.Sum[right+1] - self.Sum[left] 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 0 -2 -2 1 -4 -2 -3
