class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        stack = []
        def find_LargestSamll(num):
            l, r = 0, len(stack)-1
            while l<r:
                mid = (l+r)//2
                if stack[mid]<num:
                    l = mid+1
                else:
                    r = mid
            return r

        for num in nums: 
            # print(stack)
            if len(stack)==0 or num > stack[-1]:
                stack.append(num)
            else:
                replace_id = find_LargestSamll(num)
                stack[replace_id] = num
        return len(stack)

        
        