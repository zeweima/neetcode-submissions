class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.append(0)
        stack = [[0, -1]]

        for i in range(len(heights)):
            while stack[-1][0] > heights[i]:
                curr, _ = stack.pop()
                res = max(res, curr*(i-stack[-1][1]-1))
            stack.append([heights[i], i])
        return res