class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0
        for i in heights + [-1]: 
            stp = 0
            while stack and stack[-1][1] >= i:
                w, h = stack.pop()
                stp += w
                ans = max(ans, stp * h)

            stack.append((stp + 1, i))

        return ans