# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
        return
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.rank[parent_x]>=self.rank[parent_y]:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += self.rank[parent_y]
            else:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += self.rank[parent_x]
                
        return

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n = len(s)
        self.uf = UnionFind(n)
        for i,j in pairs:
            self.uf.union(i,j)
        
        idx = {}
        chars = {}
        for i in range(n):
            root = self.uf.find(i)
            if root not in idx:
                idx[root] = [i]
                chars[root] = [s[i]]
            else:
                idx[root].append(i)
                chars[root].append(s[i])
        
        result = [None] * n
        for rt in idx:
            sChar = sorted(chars[rt])
            for i, slot in enumerate(idx[rt]):
                result[slot] = sChar[i]
                
        result = ''.join(result)
        return result

