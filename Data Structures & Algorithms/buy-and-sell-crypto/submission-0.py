class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i,v in enumerate(prices):
            l = i+1
            while(l <= len(prices) -1):
                val = prices[l]
                result = max((val-v),result)
                l += 1
        return result