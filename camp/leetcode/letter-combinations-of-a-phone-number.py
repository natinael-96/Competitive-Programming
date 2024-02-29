class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []

        combo = []

        def backtrack(path,ind):
            if ind == len(digits):
                combo.append(path)
                return
            digit = digits[ind]
            letters = dic[digit]

            for i in letters:
                backtrack(path+i,ind+1)
        backtrack("",0)
        return combo