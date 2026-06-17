class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 

        # for the first run, calcualte the product after this nums
        for i in range(len(nums)-2,-1,-1):
            res[i] = nums[i+1] * res[i+1]
        prod = 1
        for i in range(1, len(nums)):
            prod = prod * nums[i-1]
            res[i] = res[i]*prod
        return res