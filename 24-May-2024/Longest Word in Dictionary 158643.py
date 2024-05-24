# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if not node.children[c].is_end:
                return False
            node = node.children[c]
        return True

class Solution:
    def longestWord(self, words):
        root = Trie()
        for i in words:
            root.insert(i)
        
        mx = ''

        for i in words:
            if root.search(i):
                if len(i) > len(mx) or (len(i) == len(mx) and i < mx):
                    mx = i
        
        return mx


