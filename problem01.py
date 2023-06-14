def maxProfit(prices, fee):
    n = len(prices)
    sell = [0]*n
    buy = [0]*n
    buy[0] = -prices[0]

    for i in range(1, n):
        sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)
        buy[i] = max(buy[i-1], sell[i-1] - prices[i])
    return sell[n-1]