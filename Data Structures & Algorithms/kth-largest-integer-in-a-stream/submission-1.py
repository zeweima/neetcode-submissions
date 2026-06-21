class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        if len(nums)>k:
            self.heap = nums[-k:]
        else:
            self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        if not self.heap or val > self.heap[0]:
            heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

