class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height)-1
        leftmax = height[0]
        rightmax = height[-1]
        while l<r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                res += leftmax-height[l]
            else:
                r-=1
                rightmax = max(rightmax, height[r])
                res += rightmax-height[r]
                
            # print(l,r,res)
        return res