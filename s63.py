class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, cost = 0, float('inf') #这个地方不能设置为prices[0],会报错
        for i in range(len(prices)):  #dynamische programming
            if prices[i]< cost:
                cost =prices[i]
            profit = max(profit, prices[i]- min(cost, prices[i]))
        return profit
