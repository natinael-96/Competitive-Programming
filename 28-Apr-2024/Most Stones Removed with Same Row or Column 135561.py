# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        n = len(stones)
        uf = UnionFind(n)
        if n == 1:
            return 0

        ans = 0
        xdict = defaultdict(int)
        ydict = defaultdict(int)

        for i , (x, y) in enumerate(stones):

            if x in xdict:
                ans += uf.union(i, xdict[x])
            else:
                xdict[x] = i
            
            if y in ydict:
                ans += uf.union(i, ydict[y])
            else:
                ydict[y] = i

        return ans




