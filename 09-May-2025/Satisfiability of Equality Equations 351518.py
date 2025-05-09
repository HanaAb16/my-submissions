# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Union:
    def __init__(self):
        self.size = defaultdict(int)
        self.parent = defaultdict(str)
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.size[px] += self.size[py]

    def get(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = Union()
        for eq in equations:
            v , u = eq[0] , eq[-1]
            if eq[1] == '=':
                dsu.union(v , u)
        for eq in equations:
            v , u = eq[0] , eq[-1]
            if eq[1] == '!':
                if v == u or dsu.get(v , u):
                    return False
        return True

