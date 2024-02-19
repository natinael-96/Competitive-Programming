class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        out = [0]*n

        indx = [i for i in range(n)]

        for i in sorted(deck):
            out[indx[0]] = i
            indx = indx[1:]
            if indx:
                indx.append(indx[0])
                indx = indx[1:]
            
        return out