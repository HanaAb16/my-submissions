# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Union:
    def __init__(self):
        self.size = defaultdict(int)
        self.parent = defaultdict(str)
        self.small = defaultdict(str)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.small[x] = x
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
                self.size[py] += self.size[px]
                self.small[py] = min(self.small[px] , self.small[py])
            else:
                self.parent[py] = px
                self.size[px] += self.size[py]
                self.small[px] = min(self.small[px] , self.small[py])

    def get(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = Union()
        for i in range(len(s1)):
            dsu.union(s1[i] , s2[i])
        ans = ''
        for ch in baseStr:
            ans += dsu.small[dsu.find(ch)]
        return ans

        
        