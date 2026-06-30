class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j] represent the Longest Common Subsequence of 
            text1[:i] and text2[:j]
        dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1]
                 = max(dp[i][j-1], dp[i-1][j])
        
        compress the space:
        dp[j] represent the updated longest common subsequence
        dp[j] = dp[j-1] if text1[i-1] == text2[j-1]
            we need to update from last the first (no, we should use two
            arrays)
        """
        # m, n = len(text1), len(text2)
        # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if text1[i-1]==text2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # # print(dp)
        # return dp[m][n]
        
        # m, n = len(text1), len(text2)
        # prev = [0] * (n+1)
        # curr = [0] * (n+1)
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if text1[i-1]==text2[j-1]:
        #             curr[j] = prev[j-1]+1
        #         else:
        #             curr[j] = max(prev[j],curr[j-1])
        #     prev = curr[:]
        

        # return curr[-1]
        memo = {}
        def dfs(m,n):
            if m==0 or n==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]

            if text1[m-1] == text2[n-1]:
                memo[(m,n)] = dfs(m-1,n-1)+1
            else:
                memo[(m,n)] = max(dfs(m,n-1), dfs(m-1,n))
            return memo[(m,n)]

        return dfs(len(text1), len(text2))
