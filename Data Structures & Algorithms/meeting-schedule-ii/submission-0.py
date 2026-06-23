"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        import heapq

        heap = []

        max_open = 0
        # intervals.sort()
        # print(intervals[0])
        for interval in intervals:
            a, b = interval.start, interval.end
            heapq.heappush(heap, (a, 1))
            heapq.heappush(heap, (b, -1))
        res = 0
        curr = 0
        while heap:
            _, delta = heapq.heappop(heap)
            curr += delta
            res = max(res, curr)
        return res