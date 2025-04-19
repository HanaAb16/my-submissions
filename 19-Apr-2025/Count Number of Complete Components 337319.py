# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            u , v = edge
            graph[u].append(v)
            graph[v].append(u)
        visited = [0] * n
        def dfs(node):
            v , e = 1 , 0
            for neb in graph[node]:
                e += 1
                if not visited[neb]:
                    visited[neb] = 1
                    nv , ne = dfs(neb)
                    v += nv
                    e += ne
            return v , e
        ans = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                v , e = dfs(i)
                if (e // 2) == (v * (v - 1) / 2):
                    ans += 1
        return ans