# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def toArr(rt):
            if rt is None:
                return 
            toArr(rt.left)
            arr.append(rt.val)
            toArr(rt.right)
        
        toArr(root)
        print(arr)
        
        def toBST(l, r):
            if l > r:
                return None

            mid = l + (r - l)//2
            rt = TreeNode(arr[mid])

            rt.left = toBST(l, mid - 1)
            rt.right = toBST(mid + 1, r)

            return rt
        return toBST(0, len(arr) - 1)

