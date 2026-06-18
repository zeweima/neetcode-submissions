class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = 0
        # conc = {}
        # nums.sort()
        # for num in nums:
        #     conc[num] = max(conc.get(num,0), conc.get(num-1,0)+1)
        #     res = max(res, conc[num])
        # return res
        res = 0

        range_dict = {}

        for num in nums: 
            if num-1 in range_dict:
                low_range = range_dict[num-1][0]
            else: 
                low_range = num
            if num+1 in range_dict:
                high_range = range_dict[num+1][1]
            else:
                high_range = num
            range_dict[num] = [low_range, high_range]
            range_dict[low_range][1] = high_range
            range_dict[high_range][0] = low_range
            res = max(res, high_range-low_range+1)
        return res
        
        
