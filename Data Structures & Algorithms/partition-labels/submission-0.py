class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        from collections import defaultdict
        
        max_id = defaultdict(int)
        for i, c in enumerate(s):
            max_id[c] = i
        # print(max_id)
        curr_max = 0
        last_id = -1
        res = []
        for i in range(len(s)):
            curr_max = max(curr_max, max_id[s[i]])
            if curr_max == i:
                res.append(i-last_id)
                last_id = i
        return res