class Solution:
    def simplifyPath(self, path: str) -> str:
        Stack = []

        paths = path.split("/")

        for pa in paths:
            if pa == "." or not pa:
                continue
            elif pa == "..":
                if Stack:
                    Stack.pop()
            else:
                Stack.append(pa)
                    
        return "/" + "/".join(Stack)