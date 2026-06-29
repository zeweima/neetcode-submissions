class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def get_time(k):
            time = 0
            for pile in piles:
                time += (pile+k-1)//k
            return time
        
        l, r = 1, max(piles)
        while l<=r:
            k = (l+r)//2

            if get_time(k)>h:
                l = k + 1
            else:
                r = k - 1 
        return l