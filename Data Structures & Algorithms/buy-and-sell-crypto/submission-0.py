class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        curr_min = prices[0]
        for price in prices:
            curr_min = min(price, curr_min)
            res = max(res, price- curr_min)
        return res