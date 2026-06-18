class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        valid = string.ascii_letters + string.digits
        l, r = 0, len(s)-1
        while l<r:
            while l<r and s[l] not in valid:
                l += 1
            while r>l and s[r] not in valid:
                r -= 1
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        # print(s[l-1].lower())
        return True