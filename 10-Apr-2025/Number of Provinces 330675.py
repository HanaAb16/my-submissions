# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    graph[row + 1].append(col + 1) 
        visited = [0] * (n + 1)
        def dfs(node):
            for nebr in graph[node]:
                if visited[nebr] == 1:
                    continue
                visited[nebr] = 1
                dfs(nebr)
        ans = 0
        for i in range(1 , n + 1):
            if visited[i] == 0:
                ans += 1
                visited[i] = 1
                dfs(i)
        return ans
            