sales = [12000, 15000, 18000, 14000, 20000, 22000]
profit = [3000, 4000, 5000, 3500, 6000, 7000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

total_sales = sum(sales)
total_profit = sum(profit)

print("===== SALES DASHBOARD =====")
print("Total Sales  :", total_sales)
print("Total Profit :", total_profit)

print("\nMonthly Sales:")
for i in range(len(months)):
    print(months[i], ":", sales[i])

print("\nMonthly Profit:")
for i in range(len(months)):
    print(months[i], ":", profit[i])

growth = ((sales[-1] - sales[0]) / sales[0]) * 100
print("\nGrowth :", round(growth, 2), "%")