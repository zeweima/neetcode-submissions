class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set([n])

        def update(num):
            res = 0
            while num:
                res += (num%10)**2
                num = num//10
            return res

        while n!=1:
            n = update(n)
            if n in seen:
                return False
            seen.add(n)
        return True