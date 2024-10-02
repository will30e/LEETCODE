class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1
        maxP = 0
        
        for r in range (1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
                
        return maxP
        




        