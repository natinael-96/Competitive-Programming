# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_end = True
        node.word = word
    
    def replace(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            if node.is_end:
                return node.word
        else:
            return

        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = Trie()
        for i in dictionary:
            root.insert(i)
        
        out = []
        for i in sentence.split():
            a = root.replace(i)
            #print(a)
            if a:
                out.append(a)
            else:
                out.append(i)
        
        return ' '.join(out)
        

        

        