class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Each house has two state: rob and non-rob.
        dp[i][rob] = dp[i-1][no-rob] + nums[i]
        dp[i][no-rob] = max(dp[i-1][rob],dp[i-1][no-rob])
        """

        if len(nums)==0:
            return 0
        rob = nums[0]
        no_rob = 0

        for i in range(1, len(nums)):
            rob, no_rob = no_rob+nums[i], max(rob, no_rob)
        return max(rob, no_rob)
        