# Problem: Best Time to Buy and Sell Stock
# You must buy before you sell. Return the maximum profit you can achieve.

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
