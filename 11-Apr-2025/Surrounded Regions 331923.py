# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        directions = [(1 , 0) ,  (-1 , 0) , (0 , 1) , (0 , -1)]

        def inBound(row , col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row , col):
            board[row][col] = 'Y'
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if inBound(new_row , new_col) and board[new_row][new_col] == 'O':
                    dfs(new_row , new_col)
                    
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and (r == 0 or r == n - 1 or c == 0 or c == m - 1):
                    dfs(r , c)
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
