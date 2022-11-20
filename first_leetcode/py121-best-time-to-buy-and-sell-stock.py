

class Solution:
    # 动态规划问题。
    # 思想：到当天为止，获得的最大利润，因为最小买进的已保存进行迭代。
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        min_price, max_profit = prices[0], 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit




    # 暴力法。
    # def maxProfit(self, prices: list[int]) -> int:
    #     len_prices = len(prices)
    #     max_profit = 0
    #     for split_line in range(1, len_prices):
    #         temp_min, temp_max = min(prices[: split_line]), max(prices[split_line:])
    #         if (temp_max - temp_min) > max_profit:
    #             max_profit = temp_max - temp_min
    #     return max_profit



ss = Solution()
print(ss.maxProfit([1, 4, 2]))