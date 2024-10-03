from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        Returns the maximum profit from one buy-sell transaction.

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum possible profit, or 0 if no profit can be made.
        """
        max_profit = 0  # Initialize maximum profit to zero
        buy_day = 0  # Start by assuming you buy on the first day

        # Iterate through each day starting from the second day
        for sell_day in range(1, len(prices)):
            # If current price on buy day is less than on sell day, calculate profit
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)  # Update max profit if it's higher
            else:
                # If price drops, update the buy day to the current day
                buy_day = sell_day

        return max_profit


# Example list of prices and call to the maxProfit function
prices = [7, 1, 5, 3, 6, 4, 8]
solution = Solution()
result = solution.maxProfit(prices)

# Show the result
print(f"Prices: {prices}")
print(f"Maximum Profit: {result}")
