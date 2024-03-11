class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        minAns = ''

        l, r = 0, len(letters) - 1

        while l <= r:
            mid = (l + r)//2

            if letters[mid] > target:
                minAns = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return minAns if len(minAns) > 0 else letters[0]
