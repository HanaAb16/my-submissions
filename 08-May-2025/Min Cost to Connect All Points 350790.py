# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Union:
    def __init__(self, n):
        self.size = defaultdict(int)
        self.parent = defaultdict(tuple)
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
                self.size[py] += self.size[px]
            else:
                self.parent[py] = px
                self.size[px] += self.size[py]

    def get(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    costs.append((cost , tuple(points[i]) , tuple(points[j])))
        costs.sort()
        u = Union(len(points))
        ans = 0
        for cost in costs:
            if not u.get(cost[1] , cost[2]):
                u.union(cost[1] , cost[2])
                ans += cost[0]
        return ans

                
