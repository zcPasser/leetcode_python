class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        len_prices = len(prices)
        ans = 0
        min_price = prices[0]
        for i in range(1, len_prices):
            if min_price > prices[i]:
                min_price = prices[i]
            if min_price <= prices[i] <= (min_price + fee):
                continue
            if prices[i] > (min_price + fee):
                ans += (prices[i] - min_price - fee)
                min_price = prices[i] - fee
        return ans

prices = [1, 3, 2, 8, 4, 9]
fee = 2
s = Solution()
print(s.maxProfit(prices, fee))