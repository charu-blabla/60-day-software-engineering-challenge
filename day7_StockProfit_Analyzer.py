prices = [7,1,2,3,6,4]
currentMax = 0
buy = prices[0]
buyday = 0
bestbuyday = 0
sellday = 0
for i in range(1,len(prices)):
    
    if prices[i]<buy:
        buy = prices[i]
        buyday = i
    
    profit = prices[i] - buy
    
    if profit>currentMax:
        currentMax = profit
        bestbuyday = buyday
        sellday = i
    
    
print (f"buy day : {bestbuyday}\nsell day : {sellday}\nprofit: {currentMax}")
