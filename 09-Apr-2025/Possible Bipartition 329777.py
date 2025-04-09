# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(dislikes)):
            a , b = dislikes[i]
            graph[a].append(b)
            graph[b].append(a)
        color = [-1] * (n + 1)
        def dfs(node):
            for nebr in graph[node]:
                if color[nebr] == -1:
                    color[nebr] = 1 - color[node]
                    if not dfs(nebr):
                        return False
                else:
                    if color[nebr] == color[node]:
                     
                        return False
            return True
        for i in range(1 , n + 1):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
