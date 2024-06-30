# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind():

    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.nm = n

    def find(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return 0
        
        if self.size[par_x] > self.size[par_y]:
            self.size[par_x] += self.size[par_y]
            self.parent[par_y] = par_x
        else:
            self.size[par_y] += self.size[par_x]
            self.parent[par_x] = par_y
        
        self.nm -= 1
        return 1
    
    def connected(self):
        return self.nm == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice = UnionFind(n)
        bob = UnionFind(n)

        req = 0
        
        for ty, u, v in edges:
            if ty == 3:
                req += alice.union(u, v) | bob.union(u, v)

        for ty, u, v in edges:
            if ty == 1:
                req += alice.union(u, v)
            elif ty == 2:
                req += bob.union(u, v)

        
        
        if alice.connected() and bob.connected():
            return len(edges) - req
        else:
            return -1