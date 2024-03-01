class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        peakIndex = 0
        for i in range(1, len(arr)):
            if not arr[i] > arr[i - 1]:
                peakIndex = i - 1
                break

        if peakIndex == 0:
            return False

        for i in range(peakIndex + 1, len(arr)):
            if not arr[i] < arr[i - 1]:
                return False

        return True
