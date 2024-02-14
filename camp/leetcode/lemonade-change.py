class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        tens = 0
        fives = 0

        for i in range(len(bills)):
            
            if bills[i] == 10:

                tens += 1
                fives -= 1
            if bills[i] == 5:

                fives += 1
            if bills[i] == 20:
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            print(fives, tens)

            if fives < 0:
                return False
        return True

