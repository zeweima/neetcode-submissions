class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Question: whether the array is sorted or not?
        """
        num_to_id = {}

        for idx, num in enumerate(nums):
            if target - num in num_to_id:
                return [num_to_id[target - num],idx]
            if num not in num_to_id:
                num_to_id[num] = idx
        
