def max_profit(prices):

    left, right = 0, 1
    max_profit = 0


    while right < len(prices):

        if prices[left] > prices[right]:
            left = right

        profit = prices[right] - prices[left]
        max_profit = max(max_profit, profit)

        right += 1
    return max_profit


print(max_profit([10,1,5,6,7,1]))
print(max_profit([10,8,7,5,2]))
print(max_profit([7,1,5,3,7,5,0,5]))


