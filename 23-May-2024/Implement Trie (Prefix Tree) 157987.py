# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        rt = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if rt.children[idx] is None:
                rt.children[idx] = TrieNode()
            rt = rt.children[idx]
        rt.is_end = True

    def search(self, word: str) -> bool:
        rt = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if  rt.children[idx] is None:
                return False
            rt = rt.children[idx]
        
        return rt.is_end

    def startsWith(self, prefix: str) -> bool:
        rt = self.root
        for i in prefix:
            idx = ord(i) - ord('a')
            if rt.children[idx] is None:
                return False
            rt = rt.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)