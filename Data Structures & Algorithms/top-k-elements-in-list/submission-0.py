from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        heap = []
        for num in nums:
            freq_count[num] += 1

        for key, value in freq_count.items():
            if len(heap)<k:
                heapq.heappush(heap, (value,key))
            elif value>heap[0][0]:
                heapq.heappush(heap, (value,key))
                heapq.heappop(heap)
        return [item[1] for item in heap]
