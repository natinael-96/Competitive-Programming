class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxSum = [0]

        def isBST(rt, minV=float('-inf'), maxV=float('inf')):

            if rt is None:
                return 0, True, float('inf'), float('-inf')  

            lftSum, lftBST, lftMin, lftMax = isBST(rt.left, minV, rt.val)
            rgtSum, rgtBST, rgtMin, rgtMax = isBST(rt.right, rt.val, maxV)

            if lftBST and rgtBST and lftMax < rt.val < rgtMin:
                currSum = lftSum + rgtSum + rt.val
                maxSum[0] = max(maxSum[0], currSum)
                return currSum, True, min(lftMin, rt.val), max(rgtMax, rt.val)
            else:
                return 0, False, 0, 0

        isBST(root)
        return maxSum[0]
