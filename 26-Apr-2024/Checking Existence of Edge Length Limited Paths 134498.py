# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset != yset:
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            else:
                self.parent[yset] = xset
            if self.rank[xset] == self.rank[yset]:
                self.rank[xset] += 1
            return True
        return False

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        
        for i, q in enumerate(queries):
            q.append(i)

        queries.sort(key = lambda x: x[2])
        edgeList.sort(key = lambda x: x[2])

        ans = [False] * len(queries)

        i = 0
        for q in queries:
            #print(q)
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1

            ans[q[3]]=(uf.find(q[0]) == uf.find(q[1]))
        
        return ans
                

