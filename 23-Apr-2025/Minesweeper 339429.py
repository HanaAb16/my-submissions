# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1 , 0) , (1 , 1) , (1 , -1) , (-1 , 1) , (-1 , 0) , (-1 , -1) , (0 , -1) , (0 , 1)]
        n , m = len(board) , len(board[0])
        in_bound = lambda a , b: 0 <= a < n and 0 <= b < m        
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        queue = deque([click])
        while queue:
            r , c = queue.popleft()
            adj_mines = 0
            temp = []
            if board[r][c] == 'E':
                for d in directions:
                    newr = r + d[0]
                    newc = c + d[1]
                    if in_bound(newr , newc):
                        if board[newr][newc] == 'M':
                            adj_mines += 1
                        if board[newr][newc] == 'E':
                            temp.append([newr , newc])
                if adj_mines == 0:
                    board[r][c] = 'B'
                    queue.extend(temp)
                else:
                    board[r][c] = str(adj_mines)
        return board

                

                    