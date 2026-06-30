class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap)==0:
            self.min_heap.append(num)
            return
        if self.min_heap[0]<num:
            heapq.heappush(self.min_heap,num)
            num = heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap,-num)
        if len(self.max_heap)>len(self.min_heap):
            heapq.heappush(
                self.min_heap,
                -heapq.heappop(self.max_heap)
            )
        print(self.min_heap, self.max_heap)

    def findMedian(self) -> float:
        if len(self.min_heap)>len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap)==0:
            return None
        else:
            return (self.min_heap[0]-self.max_heap[0])/2

        
    