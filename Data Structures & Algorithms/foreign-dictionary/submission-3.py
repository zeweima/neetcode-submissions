class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Info: 
            1. 'words': sorted 
            2. Return a string of the unique letters in the new alien language 
        
        Rule:
            1. 
        """
        if len(words)==0: return ""

        characters = set(words[0])
        if len(words)==1:
            return words[0]

        from collections import defaultdict

        in_degree = defaultdict(int)
        graph = defaultdict(list)
        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            characters |= set(b)

            l_a = len(a)
            l_b = len(b)
            min_l = min(l_a, l_b)
            tmp_i = 0
            while tmp_i<min_l and a[tmp_i] == b[tmp_i]:
                tmp_i += 1
            
            if tmp_i==l_b and tmp_i<l_a:
                return ""
            if tmp_i==l_a:
                continue
            if b[tmp_i] not in a[tmp_i]:
                graph[a[tmp_i]].append(b[tmp_i])
                in_degree[b[tmp_i]] +=1 
        queue = deque()
        for c in characters:
            if in_degree[c] == 0:
                queue.append(c)
        res = []

        while queue:
            curr = queue.popleft()
            res.append(curr)
            
            for nei in graph[curr]:
                in_degree[nei] -= 1
            
                if in_degree[nei] == 0:
                    queue.append(nei)
        # print(res)
        if len(res) == len(characters):
            return ''.join(res)
        return ""







