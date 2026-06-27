class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            tmp = self.permute(nums[:i]+nums[i+1:])
            # print(tmp, [item.append(nums[i]) for item in tmp])
            res.extend([item + [nums[i]] for item in tmp])
        return res