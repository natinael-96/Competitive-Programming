class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)

        if N < 2:
            return False

        for i in range(N):
            slow, fast = i, self.getNext(i, nums)

            while nums[i] * nums[fast] > 0 and nums[i] * nums[self.getNext(fast, nums)] > 0:
                if slow == fast:
                    if slow == self.getNext(slow, nums):
                        break
                    return True

                slow = self.getNext(slow, nums)
                fast = self.getNext(self.getNext(fast, nums), nums)

        return False

    def getNext(self, i, nums):
        return (i + nums[i]) % len(nums)
