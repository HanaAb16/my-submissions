# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for i in range(len(edges)):
            a , b = edges[i]
            indegree[b] += 1
        ans = []
        print(indegree)
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i) 
        if len(ans) > 1:
            return -1
        return ans[0]
        