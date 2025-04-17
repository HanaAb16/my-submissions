# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n , m= len(mat) , len(mat[0])
        directions = [(0 , 1) , (1 , 0) , (0 , -1) , (-1 , 0)]
        inbound = lambda a , b : 0 <= a < n and 0 <= b < m
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i , j))
        visited = set(queue)
        level = 1
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for d in directions:
                    newr = r + d[0]
                    newc = c + d[1]
                    if inbound(newr , newc) and (newr , newc) not in visited:
                        visited.add((newr , newc))
                        mat[newr][newc] = level
                        queue.append((newr , newc))
            level += 1
        return mat