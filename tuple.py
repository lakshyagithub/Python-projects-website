month1 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 3000, 100, 10)

max_profit = max(profits)
min_profit = min(profits)

max_profit_index = profits.index(max_profit)
min_profit_index = profits.index(min_profit)

print("Max profit index: " + str(max_profit_index) + ", Min profit index: " + str(min_profit_index))
max_month = month1[max_profit_index]
min_month = month1[min_profit_index]

print("Max profit made in: " + max_month + ". Profit made: " + str(max_profit))
print("Min profit made in: " + min_month + ". Profit made: " + str(min_profit))