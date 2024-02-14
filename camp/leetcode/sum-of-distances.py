class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        occur = defaultdict(list)
        out = [0]*len(nums)

        for i,ch in enumerate(nums):
            occur[ch].append(i)
        
        for indx in occur.values():
            lf, rg = 0, sum(indx) - len(indx)*indx[0]

            for j in range(len(indx)):
                out[indx[j]] = lf + rg

                if j + 1 < len(indx):
                    lf += (indx[j+1] - indx[j])*(j+1)
                    rg -= (indx[j+1] - indx[j])*(len(indx) - j - 1)

        return out
