# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset != yset:
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            else:
                self.parent[yset] = xset
            if self.rank[xset] == self.rank[yset]:
                self.rank[xset] += 1
            return True
        return False

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emails = defaultdict(int)

        for idx, acc in enumerate(accounts):
            for i in acc[1:]:
                if i not in emails:
                    emails[i] = idx
                else:
                    uf.union(idx, emails[i])

        print(emails)

        acc = defaultdict(list)

        for email, idx in emails.items():
            par = uf.find(idx)
            acc[par].append(email)

        print(acc)
        
        return [[accounts[i][0]] + sorted(email) for i, email in acc.items()]
