
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        cost = 0
        n = len(points)
        distance = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n-1):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
                distance[i][j] = dist
                distance[j][i] = dist
        
        visited = set([0])
        heap = []
        for i in range(1,n):
            heap.append((distance[0][i],i))
        heapq.heapify(heap)
        # print(distance)
        while len(visited)<n:
            while heap[0][1] in visited:
                heapq.heappop(heap)
            dis, new_node = heapq.heappop(heap)
            # print(dis, new_node, heap)
            cost +=dis
            visited.add(new_node)
            for i in range(n):
                if i not in visited:
                    heapq.heappush(heap,(distance[i][new_node],i))
        return cost
