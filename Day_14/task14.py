
def count_stair_ways(n):
    memo = {}
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = count_stair_ways(n - 1) + count_stair_ways(n - 2)
    return memo[n]

n = int(input("Enter number of stairs: "))
ways = count_stair_ways(n)
print("Number of ways: ", ways)

################################################
#test cases:
# S 1 = 1 and S 2 = 2 ,
# S 3 = 3 , S 4 = 5 , S 5 = 8 ,
# S 6 = 13 , S 7 = 21 , S 8 = 34 , S 9 = 55 ,
# S 10 = 89 , S 11 = 144 , and S 12 = 233 .

def maxProfit(prices):
  """
  Finds the maximum profit from buying and selling a stock once.

  Args:
    prices: A list of integers representing the stock prices.

  Returns:
    The maximum profit achievable.
  """

  max_profit = 0
  min_price = float('inf')

  for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(max_profit, profit)

  return max_profit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))

