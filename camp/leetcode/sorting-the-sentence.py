class Solution:
    def sortSentence(self, s: str) -> str:
        ss = s.split()
        sentence = [None]*len(ss)
        for i in ss:
            indx = int(i[-1]) - 1
            wrd = i[:-1]
            sentence[indx] = wrd
        
        return " ".join(sentence)
