class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #LC 121 - Best Time to Buy and Sell Stock
        res = 0
        lowest = prices[0]

        for p in prices:
            if p<lowest:
                lowest = p
            
            res = max(res,p-lowest)

        return res
        