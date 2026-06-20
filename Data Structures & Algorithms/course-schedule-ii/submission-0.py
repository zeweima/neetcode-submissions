class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        next_class = [[] for _ in range(numCourses)]

        n_pre = [0] * numCourses

        for a, b in prerequisites:
            n_pre[a] += 1
            next_class[b].append(a)

        res = []
        queue = []
        for i in range(numCourses):
            if n_pre[i]==0:
                queue.append(i)
        
        while queue:
            t_class = queue.pop()
            res.append(t_class)
            for next_c in next_class[t_class]:
                n_pre[next_c] -= 1
                if n_pre[next_c] == 0:
                    queue.append(next_c)
        # print(n_pre)
        if len(res) == numCourses:
            return res 
        return []
