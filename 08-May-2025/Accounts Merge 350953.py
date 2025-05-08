# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Union:
    def __init__(self):
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uni = Union()
        for acc in accounts:
            name = acc[0]
            if len(acc) > 2:
                for i in range(2 , len(acc)):
                    if not uni.get((name , acc[i - 1]) , (name , acc[i])):
                        uni.union((name , acc[i - 1]) , (name , acc[i]))
            else:
                uni.find((name , acc[1]))

        graph = defaultdict(list)
        for key , val in uni.parent.items():
            graph[uni.find(val)].append(key[1])
       
        ans = []
        for key , val in graph.items():
            ans.append([key[0]] + sorted(val))
        return ans
        
                    