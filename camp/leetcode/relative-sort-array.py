from collections import defaultdict
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        c1 = defaultdict(list)
        for elem in arr1:
            c1[elem].append(1)

        answer = list()
        for elem in arr2:
            answer.extend([elem]*len(c1[elem]))
            
        remaining = list()
        for elem in arr1:
            if elem not in arr2:
                remaining.append(elem)

        remaining.sort()

        return answer + remaining
