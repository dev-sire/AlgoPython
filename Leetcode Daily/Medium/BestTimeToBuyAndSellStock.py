from ast import List
from math import inf

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        profit = [0] * (k + 1)
        buy = [-inf] * (k + 1)
        sell = [-inf] * (k + 1)
        for price in prices:
            prev = profit[0]
            for i in range(1, k + 1):
                p = profit[i]
                profit[i] = max(profit[i], buy[i] + price, sell[i] - price)
                buy[i] = max(buy[i], prev - price)
                sell[i] = max(sell[i], prev + price)
                prev = p
        return max(profit)