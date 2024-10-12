class Solution:
        #Create a max profit counter 
    # iterate through the length of the prices starting from 1
    # if the second days prices is bigger than the previous days price then we know there is profit made
    # create a profit variable that will calculate by subtracting the current from the previous day
    # keep adding the profit to the max Profit
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i -1]:
                profit = prices[i] - prices[i - 1]
                maxp += profit
                
                
        return maxp
        