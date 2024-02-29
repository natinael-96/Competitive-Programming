class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        flip = [i[::-1] for i in image]

        revert = []
        for i in flip:
            revert.append([x^1 for x in i])
        
        return revert

