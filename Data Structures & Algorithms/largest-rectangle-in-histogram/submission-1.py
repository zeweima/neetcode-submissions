class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # res = 0
        # heights.append(0)
        # stack = [[0, -1]]

        # for i in range(len(heights)):
        #     while stack[-1][0] > heights[i]:
        #         curr, _ = stack.pop()
        #         res = max(res, curr*(i-stack[-1][1]-1))
        #     stack.append([heights[i], i])
        # return res

        res = 0
        n = len(heights)
        RightEdge = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                curr_i = stack.pop()
                RightEdge[curr_i] = i
            stack.append(i)
        
        leftEdge = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]]>heights[i]:
                curr_i = stack.pop()
                leftEdge[curr_i] = i
            stack.append(i)
        print(RightEdge)
        print(leftEdge)
        res = 0
        for i in range(n):
            res = max(res, heights[i] * (RightEdge[i]-leftEdge[i]-1))
        return res
