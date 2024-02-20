class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) <= 2:
            return 0

        leftMax, rightMax = 0, 0
        left, right = 0, len(height) - 1
        trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    trapped += max(leftMax - height[left], 0)
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    trapped += max(rightMax - height[right], 0)
                right -= 1

        return trapped