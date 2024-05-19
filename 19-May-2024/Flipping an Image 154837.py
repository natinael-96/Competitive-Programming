# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            image[i] = image[i][::-1]
        
        for i in range(n):
            for j in range(n):
                image[i][j] = image[i][j] ^ 1
        
        return image