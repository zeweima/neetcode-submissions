class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key=lambda x: x[0])
        curr_right = None
        for a, b in intervals:
            if curr_right is None:
                curr_right = b
                continue
            if a<curr_right:
                res +=1
                curr_right = min(curr_right, b)
            else:
                curr_right = b
        return res