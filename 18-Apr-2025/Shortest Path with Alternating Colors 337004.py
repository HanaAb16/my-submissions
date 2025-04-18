# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)
        for edge in redEdges:
            a , b = edge
            redGraph[a].append(b) 
        for edge in blueEdges:
            a , b = edge
            blueGraph[a].append(b) 

        queue = deque([(0 , 'red') , (0 , 'blue')])
        visited = [[False , False] for _ in range(n)]
        visited[0][0] = visited[0][1] = True
        ans = [-1] * n
        ans[0] = 0
        level = 1

        while queue:
            for _ in range(len(queue)):
                node , color = queue.popleft()
                if color == 'red':
                    neighbours = blueGraph[node]
                    next_color = 'blue'
                    color_ind = 1
                else:
                    neighbours = redGraph[node]
                    next_color = 'red'
                    color_ind = 0
                for neb in neighbours:
                    if not visited[neb][color_ind]:
                        visited[neb][color_ind] = True
                        queue.append((neb , next_color))
                        if ans[neb] == -1:
                            ans[neb] = level
            level += 1
        return ans
        
        