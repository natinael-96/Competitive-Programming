class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicT = set(nums1)
        
        result = []
        for num in nums2:
            if num in dicT:
                result.append(num)
                dicT.remove(num)
        
        return result

