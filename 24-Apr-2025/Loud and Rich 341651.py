# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = set(quiet)
        for u , v in richer:
            graph[v].append(u)
            indegree.discard(u)
        visited = [0] * len(quiet)
        ans = [0] * len(quiet)
        def dfs(node):
            least = node
            for neb in graph[node]:
                if not visited[neb]:
                    visited[neb] = 1
                    temp = dfs(neb)
                    if quiet[temp] < quiet[least]:
                        least = temp
                else:
                    if quiet[least] > quiet[ans[neb]]:
                        least = ans[neb]
            ans[node] = least
            return least
        for i in indegree:
            if not visited[i]:
                visited[i] = 1
                dfs(i)
        return ans
                
        