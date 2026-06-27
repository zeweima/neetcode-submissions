class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict

        memo = defaultdict(list)
        memo[0] = [[]]
        for num in nums:
            for value in range(target+1):
                if value in memo:
                    for curr_list in memo[value]:
                        memo[value+num].append(curr_list+[num])
        return memo[target]