class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # swap_i = 0
        while nums[0]!=nums[nums[0]]:
            tmp = nums[nums[0]] 
            nums[nums[0]] = nums[0]
            nums[0] = tmp
            # nums[0], nums[nums[0]] = nums[nums[0]], nums[0]
            # swap_i +=1 
            # print(nums)
            # if swap_i == 5:
            #     break
        return nums[0]

                