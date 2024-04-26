# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list) 
        deg = defaultdict(int)

        for i in range((len(ingredients))):
            for j in ingredients[i]:
                graph[j].append(recipes[i])
                deg[recipes[i]] += 1

        for sup in supplies:
            deg[sup] = 0
        
        ans = []
        q = deque()
        for i in deg.keys():
            if deg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for i in graph[node]:
                deg[i] -= 1

                if deg[i] == 0:
                    q.append(i)
                    
                    if i in recipes:
                        ans.append(i)

        return ans