class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            interval1 = firstList[i]
            interval2 = secondList[j]
            
            if interval1[0] > interval2[0]:
                start = interval1[0]
            else:
                start = interval2[0]
            
            end = min(interval1[1], interval2[1])
            
            if start <= end:
                result.append([start, end])
            
            if end == interval1[1]:
                i += 1
            
            if end == interval2[1]:
                j += 1
        
        return result
