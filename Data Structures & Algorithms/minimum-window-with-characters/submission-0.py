class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c_count = {}

        for c in t:
            c_count[c] = c_count.get(c, 0)+1
        
        l=0
        res = s+'#'
        n_remain = len(t)
        for r in range(len(s)):
            if s[r] in c_count:
                if c_count[s[r]]>0:
                    n_remain -= 1
                c_count[s[r]]-=1
            
            while n_remain == 0:
                if r-l+1 < len(res):
                    res = s[l:r+1]
                if s[l] in c_count:
                    if c_count[s[l]]>=0:
                        n_remain += 1
                    c_count[s[l]]+=1
                l+=1
            # print(n_remain, c_count, res)
        if len(res) < len(s)+1:
            return res
        else:
            return ''