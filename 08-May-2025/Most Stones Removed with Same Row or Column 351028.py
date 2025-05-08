# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Union:
    def __init__(self, n):
        self.size = [1] * (n)
        self.parent = [i for i in range(n)]

    def find(self, x):
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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        u = Union(n)
        for i in range(n):
            for j in range(i + 1 , n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    u.union(i , j)
        ans = 0
        for i in range(n):
            if i != u.parent[i]:
                ans += 1
        return ans

        