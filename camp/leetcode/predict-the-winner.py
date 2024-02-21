class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(A , B, arr, player):

            if len(arr) == 0:
                return A >= B
            
            if player == 1:
                ch1 = arr[0]
                ch2 = arr[-1]

                return predict(A + ch1, B, arr[1:], 2) or predict(A + ch2, B, arr[:-1], 2)
            else:
                ch1 = arr[0]
                ch2 = arr[-1]

                return predict(A, B + ch1, arr[1:], 1) and predict(A, B + ch2, arr[:-1], 1)
        return predict(0, 0, nums, 1)
                

