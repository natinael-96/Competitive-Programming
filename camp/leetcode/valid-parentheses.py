class Solution:
    def isValid(self, s: str) -> bool:
        left ={"(","{","["}

        Stack = []

        for i in (s):
            if i in "[{(" or not Stack:
                Stack.append(i)
            else:
                if ((i == ")" and Stack[-1] == "(") or 
                (i == "}" and Stack[-1] == "{") or
                (i == "]" and Stack[-1] == "[")):
                    Stack.pop()
                else:
                    return False
        return len(Stack) == 0

            