# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if root is None:
            return ans
        
        
        sameDep = defaultdict(list)

        def travers(rt,dpth):
            if not rt:
                return 
            sameDep[dpth].append(rt.val)

            travers(rt.left, dpth+1)
            travers(rt.right, dpth + 1)

        travers(root, 0)
        for i in sameDep.keys():
            cur = sameDep[i]
            if i % 2:
                ans.append(cur[::-1])
            else:
                ans.append(cur)

        return ans
            
            