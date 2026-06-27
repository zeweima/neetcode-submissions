class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # from collections import defaultdict

        # memo = defaultdict(list)
        # memo[0] = [[]]
        # for num in nums:
        #     for value in range(target+1):
        #         if value in memo:
        #             for curr_list in memo[value]:
        #                 memo[value+num].append(curr_list+[num])
        # return memo[target]

        res = []

        def dfs(i, curr_path, total):
            if total==target:
                res.append(curr_path[:])
                return
            if total> target:
                return
            
            for j in range(i, len(nums)):
                curr_path.append(nums[j])
                dfs(j, curr_path, total+nums[j])
                curr_path.pop()
        
        dfs(0, [], 0)
        return res




