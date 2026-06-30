class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        
        for a, b in prerequisites:
            graph[b] = graph.get(b, [])
            graph[b].append(a)

        visited = set()
        visiting = set()
        # print(graph)
        def dfs(node):
            # cycle detection
            # print('dfs', node, visiting)
            if node in visited:
                return False
            if node in visiting:
                # print(node, visiting)
                return True
            visiting.add(node)
            # print(graph.get(node, []))
            for child in graph.get(node, []):
                
                if dfs(child):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False
        
        for node in graph:
            print(node)
            if node not in visited and dfs(node):
                return False
            # visited.add(node)
        return True