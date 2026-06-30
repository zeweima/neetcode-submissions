class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) == 0:
            return 0
        res = 0
        target_c = (1, s[0])
        c_count = {s[0]:1}

        l = 0
        for r in range(1, len(s)):
            c_count[s[r]] = c_count.get(s[r],0)+1

            if c_count[s[r]]>=target_c[0]:
                target_c = (c_count[s[r]], s[r])
            # print(c_count)
            # print(l,r, target_c)
            if r-l+1-target_c[0]>k:
                c_count[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)
        return res