class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Greedy approach: each time burst the smallest ballons
        """
        nums= [1] + nums + [1]

        memo = {}

        def dfs(l,r):

            if (l,r) in memo:
                return memo[(l,r)]
            max_coins = 0
            for i in range(l+1,r):
                max_coins = max(
                    max_coins,
                    dfs(l,i) + dfs(i,r) + nums[l]*nums[i]*nums[r]
                )
            memo[(l,r)] = max_coins
            return max_coins
        
        return dfs(0,len(nums)-1)