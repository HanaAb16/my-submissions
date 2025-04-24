# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        ans = []
        def dfs(node):
            color[node] = 1
            for neb in graph[node]:
                if color[neb] == 1:
                    return False
                if color[neb] == 0:
                    if not dfs(neb):
                        return False
            ans.append(node)
            color[node] = 2
            return True
        for i in range(n):
            if color[i] == 0:
                dfs(i)
        return sorted(ans)