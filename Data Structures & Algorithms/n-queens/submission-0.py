class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        grid = [['.' for _ in range(n)] for _ in range(n)]
        def dfs(i):
            if i == n:
                tmp = [''.join(row) for row in grid]
                res.append(tmp)
            
            for j in range(n):
                if (j not in col) and (i+j not in add) and (i-j not in diff):
                    grid[i][j] = 'Q'
                    col.add(j)
                    add.add(i+j)
                    diff.add(i-j)
                    dfs(i+1)
                    
                    grid[i][j] = '.'
                    col.remove(j)
                    add.remove(i+j)
                    diff.remove(i-j)
        
        col = set()
        add = set()
        diff = set()
        dfs(0)
        # print(res)
        return res