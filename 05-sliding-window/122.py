def max_profit(prices):

    left, right = 0, 1
    profit = 0


    while right < len(prices):

        if prices[left] < prices[right]:
            profit += prices[right] - prices[left]
        left += 1
        right += 1
            
    return profit


print(max_profit([10,1,5,6,7,1]))
print(max_profit([10,8,7,5,2]))
print(max_profit([7,1,5,3,7,5,0,5]))


