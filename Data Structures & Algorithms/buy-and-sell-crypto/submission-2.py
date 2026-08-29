# 10, 1, 5, 6, 7, 1
# 10  1. 1. 1. 1. 1
# 7   7  7  7  1  1
# -3  6  6. 6  0. 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit
        
