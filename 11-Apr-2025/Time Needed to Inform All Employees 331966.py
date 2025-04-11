# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        def dfs(node):
            time = 0
            for nebr in graph[node]:
                time = max(dfs(nebr) , time)
            return informTime[node] + time
        return dfs(headID)