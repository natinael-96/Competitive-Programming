# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        mxNm = max(nums)
        mxInd = nums.index(mxNm)
        root = TreeNode(mxNm)

        root.left = self.constructMaximumBinaryTree(nums[:mxInd])

        root.right = self.constructMaximumBinaryTree(nums[mxInd+1:])

        return root