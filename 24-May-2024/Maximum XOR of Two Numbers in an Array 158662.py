# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.val = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, n):
        rt = self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if rt.children[bit] is None:
                rt.children[bit] = TrieNode()
            rt = rt.children[bit]
        rt.val = n

class Solution:
    def findMaximumXOR(self, nums):
        tr = Trie()
        for num in nums:
            tr.add(num)
        
        mx = 0
        for num in nums:
            rt = tr.root
            cur = 0
            for j in range(31, -1, -1):            
                bit = (num >> j) & 1
                t_bit = 1 - bit
                if rt.children[t_bit] is not None:
                    cur = (cur << 1) | 1
                    rt = rt.children[t_bit]
                else:
                    cur = (cur << 1) | 0
                    rt = rt.children[bit]
            mx = max(mx, cur)
        return mx
