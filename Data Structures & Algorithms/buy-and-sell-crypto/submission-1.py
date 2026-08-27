# 10, 1, 5, 6, 7, 1
# 10  1. 1. 1. 1. 1
# 7   7  7  7  1  1
# -3  6  6. 6  0. 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0

        while buy < len(prices) and sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell

            sell += 1

        return max_profit

        # min_prices = [prices[0]]
        # max_prices = [prices[-1]]

        # for i in range(1, len(prices)):
        #     if prices[i] < min_prices[i - 1]:
        #         min_prices.append(prices[i])
        #     else:
        #         min_prices.append(min_prices[i - 1])

        # prices.reverse()

        # for i in range(1, len(prices)):
        #     if prices[i] > max_prices[i - 1]:
        #         max_prices.append(prices[i])
        #     else:
        #         max_prices.append(max_prices[i - 1])

        # max_prices.reverse()

        # diff = []

        # for i in range(0, len(prices)):
        #     diff.append(max_prices[i] - min_prices[i])

        # return max(diff)

