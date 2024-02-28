# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def srtArr(left, right):
            if left > right:
                return None
            mid = (left + right)//2
            rt = TreeNode(nums[mid])
            rt.left = srtArr(left,mid-1)
            rt.right = srtArr(mid + 1, right)

            return rt
        return srtArr(0, len(nums) -1)

            



