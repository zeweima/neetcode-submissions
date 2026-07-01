class Solution:
    def jump(self, nums: List[int]) -> int:
        # min_step = [float('inf')] * n
        # min_step[0] = 0
        # for i in range(len(nums)):
        #     for j in range(1,num[i]):
        #         if i+j<len(nums):
        #             min_step[i+j] = min(min_step[i+j], min_step[i]+1)
        # if min_step[-1]<float('inf'):
        #     return min_step[-1]
        # return -1
        max_range = 0
        step = 0
        pre_range = 0
        curr_range = 0
        while max_range<len(nums)-1:
            for i in range(pre_range, curr_range+1):
                max_range = max(max_range, i+nums[i])
            pre_step = curr_range+1
            curr_range = max_range
            step+=1 
        return step
