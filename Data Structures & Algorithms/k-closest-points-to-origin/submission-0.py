class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            return math.sqrt(point[0]*point[0]+point[1]*point[1])
        
        distance = [[distance(point), point] for point in points]
        heapq.heapify(distance)

        return [heapq.heappop(distance)[1] for _ in range(k)]
        