# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Union:
    def __init__(self , n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def find(self , x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.parent[self.parent[x]]
        return self.find(self.parent[x])
    
    def union(self , x , y):
        parentx = self.find(x)
        parenty = self.find(y)
        if parentx != parenty:
            if self.size[parentx] < self.size[parenty]:
                self.parent[parentx] = parenty
                self.size[parenty] += self.size[parentx]
            elif self.size[parentx] > self.size[parenty]:
                self.parent[parenty] = parentx
                self.size[parentx] += self.size[parenty]
            else:
                self.parent[parentx] = parenty
                self.size[parenty] += self.size[parentx]
    def get(self , x , y):
        parentx = self.find(x)
        parenty = self.find(y)
        if parentx == parenty:
            return True
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uni = Union(len(edges))
        for u , v in edges:
            if uni.get(u , v):
                return [u , v]
            uni.union(u , v)