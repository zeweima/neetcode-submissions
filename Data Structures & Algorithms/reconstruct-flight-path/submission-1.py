class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # from collections import defaultdict
        # graph = defaultdict(dict)
        # tickets.sort(key=lambda x: x[1])

        # for src, des in tickets:
        #     if des in graph[src]:
        #         graph[src][des] += 1
        #     else:
        #         graph[src][des] = 1
        
        # path = ['JFK']
        # # print(graph)
        # def dfs(src):
        #     if len(path) == len(tickets)+1:
        #         return True
        #     for nei in graph[src]:
        #         # print(nei)
        #         if graph[src][nei]>0:
        #             path.append(nei)
        #             graph[src][nei]-=1
        #             print(path)
        #             if dfs(nei):
        #                 return True
        #             path.pop()
        #             graph[src][nei]+=1
        #     return False
        # dfs('JFK')
        # # print(path)
        # return path

        from collections import defaultdict

        graph = defaultdict(list)
        tickets.sort(reverse=True)

        for out_node, in_node in tickets:
            graph[out_node].append(in_node)
        res = []

        def dfs(node):

            while graph[node]:
                curr = graph[node].pop()
                dfs(curr)
            res.append(node)
        dfs('JFK')
        return res[::-1]