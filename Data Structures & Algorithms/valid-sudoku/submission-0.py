class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        The idea is to use some identifier to take down the appearance
        using backracking approaches.
        """

        row_log = [0]*9
        col_log = [0]*9

        square_log = [[0 for _ in range(3)] for _ in range(3)]

        # update log:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                s_i = i//3
                s_j = j//3
                if (((1<<int(board[i][j]))&row_log[i])==0 and 
                    ((1<<int(board[i][j]))&col_log[j])==0 and 
                    ((1<<int(board[i][j]))&square_log[s_i][s_j])==0):
                    
                    row_log[i] += 1<<int(board[i][j])
                    col_log[j] += 1<<int(board[i][j])
                    square_log[s_i][s_j] += 1<<int(board[i][j])
                else:
                    return False
        return True
        # def dfs(idx):
        #     if idx==81: return True
            
        #     i = idx//9
        #     j = idx%9
            
        #     if board[i][j]=='.':
        #         for num in range(1,10):
        #             s_i, s_j = i//3, j//3

        #             if (((1<<num)&row_log[i])==0 and 
        #                 ((1<<num)&col_log[j])==0 and 
        #                 ((1<<num)&square_log[s_i][s_j])==0):
        #                 row_log[i] += 1<<num
        #                 col_log[j] += 1<<num
        #                 square_log[s_i][s_j] += 1<<num
        #                 if dfs(idx+1): 
        #                     return True
        #                 row_log[i] -= 1<<num
        #                 col_log[j] -= 1<<num
        #                 square_log[s_i][s_j] -= 1<<num
        #         return False
        #     else:
        #         return dfs(idx+1)
        # return dfs(0)


