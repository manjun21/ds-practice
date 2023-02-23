#https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/
def maxProfit(prices) -> int:
    profit = 0
    i = 0
    while i < len(prices):
        j = i +1
        while j < len(prices)-1: 
            if prices[i] < prices[j]:
                print(prices[i])
                print(prices[j])
                diff = prices[j] - prices[i]
                profit = profit + diff
                i = i + 1
                break
            else:
                j = j+ 1
        i = i +1      
    print(profit)

#prices = [7,1,5,3,6,4]
#Output: 7

#prices = [1,2,3,4,5]

prices = [7,6,4,3,1]
maxProfit(prices)