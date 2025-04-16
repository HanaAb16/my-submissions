# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        
        def bfs(queue):
            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if color[child] == color[node]:
                        return False
                    if color[child] == -1:
                        color[child] = 1 - color[node]
                        queue.append(child)
            return True
            
        for i in range(len(graph)):
            if  color[i] == -1:
                queue = deque([i])
                color[i] = 0
                if not bfs(queue):
                    return False
        return True

        

