class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        from collections import deque

        graph = defaultdict(dict)
        for u,v in edges:
            graph[u][v] = 1
            graph[v][u] = 1
        
        visited = set()
        queue = deque()

        # for i in range(n):
        #     if i in visited:
        #         continue
        visited.add(0)
        queue.append(0)
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if graph[curr][neighbor] == 1:
                    if neighbor in visited: return False
                    graph[curr][neighbor] = 0
                    graph[neighbor][curr] = 0
                    queue.append(neighbor)
                    visited.add(neighbor)
        return len(visited)==n




