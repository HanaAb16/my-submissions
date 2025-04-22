# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1] , values[i]))
            graph[equations[i][1]].append((equations[i][0] , (1 / values[i])))
        def bfs(start , end):
            visited = set()           
            queue = deque([(start , 1.0)])
            visited.add(start)
            while queue:
                node , val = queue.popleft()
                if node == end:
                    return val
                for neb , weight in graph[node]:
                    if neb not in visited:
                        visited.add(neb)
                        queue.append((neb , val * weight))
            return -1.0
        ans = []
        for query in queries:
            start , end = query
            if start in graph.keys():
                ans.append(bfs(start , end))
            else:
                ans.append(-1.0)
        return ans 
