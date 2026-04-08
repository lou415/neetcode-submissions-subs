class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # int array of prices; prices[i] = NeetCoin Price on the ith day.
        # choose a single day to buy, and a single day to sell in the future.
        # choose the day you can buy and sell to make the maximum profit.
        # profit = buy price - sell price

        # some internal storage to hold values?

        max_profit = 0

        if not prices:
            return 0

        L = prices[0]

        for price in prices:
            if L > price:
                L = price
            if L < price:
                # get the difference
                current_profit = price - L
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit