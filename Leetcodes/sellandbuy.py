class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        least_stock_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < least_stock_price:
                least_stock_price = price
            elif price - least_stock_price > max_profit:
                max_profit = price - least_stock_price

        return max_profit