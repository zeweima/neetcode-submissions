class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        res = []
        while l<len(nums)-2:
            two_res = self.twosum(l+1, -nums[l], nums)
            for item in two_res:
                res.append([nums[l]]+item)
            l+=1
            while l<len(nums)-2 and nums[l]==nums[l-1]:
                l+=1
        return res
    
    def twosum(self, l, target, nums):
        r = len(nums)-1
        res = []
        while l<r:
            if nums[l]+nums[r] == target:
                res.append([nums[l], nums[r]])
                l+=1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
            if l<r and nums[l]+nums[r] < target:
                l += 1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
            if r>l and nums[l]+nums[r] > target:
                r -= 1
                while l<r and nums[r] == nums[r+1]:
                    r-=1
        return res