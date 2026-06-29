class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m, n = len(s), len(p)

        # dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

        # dp[0][0] = True

        # for j in range(1,n+1):
        #     if p[j-1] == '*':
        #         dp[0][j] = dp[0][j-2]
        
        # for i in range(1, m+1):
        #     for j in range(1,n+1):
        #         if p[j-1]=='*':
        #             dp[i][j] = dp[i][j-2]
        #             if p[j-2]=='.' or p[j-2]==s[i-1]:
        #                 dp[i][j] |= dp[i-1][j]
        #         else:
        #             if p[j-1]=='.' or p[j-1]==s[i-1]:
        #                 dp[i][j] = dp[i-1][j-1]
        # return dp[m][n]

        memo = {}

        def dfs(m,n):
            if n == 0:
                return m == 0
            
            if (m,n) in memo:
                return memo[(m,n)]

            if p[n-1] == '*':
                if dfs(m,n-2):
                    memo[(m,n)] = True
                    return True
                if p[n-2] == '.' or p[n-2] == s[m-1]:
                    if dfs(m-1,n):
                        memo[(m,n)] = True
                        return True
            else:
                if p[n-1] == '.' or p[n-1] == s[m-1]:
                    if dfs(m-1,n-1):
                        memo[(m,n)] = True
                        return True 
            memo[(m,n)] = False
            return memo[(m,n)]

        return dfs(len(s), len(p))
