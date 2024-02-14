class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        road= [0]*1001

        for i in trips:
            numP,fro , toi = i[0], i[1], i[2]

            road[fro] += numP
            road[toi] -= numP
        tot = 0
        for i in range(1001):
            tot += road[i]
            if tot > capacity:
                return False
        
        return True