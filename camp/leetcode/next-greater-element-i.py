class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
         
        lastInd = defaultdict(int)
        
        stack = [nums2[0]]

        for i in range(1,len(nums2)):

            while stack and nums2[i] > stack[-1]:
                lastInd[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        out = []
        for i in range(len(nums1)):
            if nums1[i] in lastInd:
                out.append(lastInd[nums1[i]])
            else:
                out.append(-1)


        return out           
