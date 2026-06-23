class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m,n = len(matrix), len(matrix[0])
        mas_length = 0
        memo = {}

        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            deltas = [(1,0), (-1,0), (0,1), (0,-1)]

            max_depth = 1
            for di, dj in deltas:
                next_i, next_j = i+di, j+dj
                if 0<= next_i<m and 0<=next_j<n and matrix[i][j]<matrix[next_i][next_j]:
                    max_depth = max(max_depth, dfs(next_i, next_j)+1)

            memo[(i,j)] = max_depth
            return max_depth
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        return res