class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_numbers = []
        negative_numbers = []
        result = []
        
        for num in nums:
            if num >= 0:
                positive_numbers.append(num)
            else:
                negative_numbers.append(num)  
        
        for i in range(len(positive_numbers)):
            result.append(positive_numbers[i])
            result.append(negative_numbers[i])
        
        return result
