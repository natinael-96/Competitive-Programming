# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        dicT = defaultdict(int)

        def travers(rt):
            if rt is None:
                return 
            
            dicT[rt.val]+=1
            travers(rt.left)
            travers(rt.right)
        travers(root)

        mode = []

        maxFreq = max(dicT.values())
        for i in dicT.keys():
            if dicT[i] == maxFreq:
                mode.append(i)
        return mode