import math

class Solution:
    def reverse(self, x: int) -> int:
        # if x<0:
        #     x = -x
        #     sign = -1
        # else:
        #     sign = 1
        
        # res = 0
        # max_value = 2**31 - 1
        # while x>0:
        #     if sign ==1 and (max_value - x%10)/10<res:
        #         return 0
        #     if sign == -1 and (max_value - x%10+1)/10<res:
        #         return 0
        #     res = res*10 + x%10
        #     x = x//10
        # return res * sign

        min_value = -2**31
        max_value = 2**31 - 1

        res = 0 
        while x!=0:
            digit = int(math.fmod(x, 10))

            x = int(x/10)
            if res<0 and res < (min_value - digit)/10:
                return 0
            if res>0 and res > (max_value - digit)/10:
                return 0

            res = res*10 + digit
        return res