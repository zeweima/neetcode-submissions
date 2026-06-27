class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # if len(s)==0:
        #     return 0

        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in count or count[s[r]]==0:
                count[s[r]]=1
                res = max(res, r-l+1)
            else:
                while count[s[r]]==1:
                    count[s[l]]-=1
                    l+=1
                count[s[r]]+=1
        return res