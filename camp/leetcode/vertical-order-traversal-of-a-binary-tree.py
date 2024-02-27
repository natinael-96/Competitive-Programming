# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        sameLevel = defaultdict(list)

        def travers(rt, vert, depth):
            if rt:
                travers(rt.left, vert - 1, depth + 1)
                sameLevel[vert].append([rt.val, depth])
                travers(rt.right, vert + 1, depth + 1)
        
        travers(root, 0,0)
        ans = []
        for i in sorted(sameLevel.keys()):
            ans.append([j[0] for j in sorted(sameLevel[i], key=lambda x:(x[1] , x[0]))])

        return ans