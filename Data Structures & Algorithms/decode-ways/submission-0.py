class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dp[i] = 0
        dp[i] += dp[i-1] if s[i-1] is valid
        dp[i] += dp[i-2] of s[i-1:i] is valid
        if dp[i] == 0 return 0
        """
        
        def check_valid(num):
            if len(num) == 2 and num[0] == '0':
                return False

            if 0<int(num)<27:
                return True 
            else:
                return False

        memo = {}
        n = len(s)
        def dfs(i):
            if i in memo:
                return memo[i]

            if i==n: return 1
            
            res = 0
            # print(i)
            if check_valid(s[i]):
                res += dfs(i+1)
            if i+1<n and check_valid(s[i:i+2]):
                res += dfs(i+2)
            memo[i] = res 
            return res 
        return dfs(0)
            

            