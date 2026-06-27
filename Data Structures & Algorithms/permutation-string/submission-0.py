class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c,0)+1
        
        l = 0
        tmp_count = s1_count.copy()
        for r,c in enumerate(s2):
            if c not in tmp_count:
                l = r+1
                tmp_count = s1_count.copy()
                continue
            tmp_count[c] -=1
            while tmp_count[c]<0:
                tmp_count[s2[l]] += 1
                l+=1
            if r-l+1 == len(s1):
                return True 
            
        return False


