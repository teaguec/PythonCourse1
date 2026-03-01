sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w1.append(int(input("Enter last day sales: ")))

total_sales = sales_w1 + sales_w2

best_day = max(total_sales) * 1.50
worst_day = min(total_sales) * 1.50

print(total_sales)
print(best_day)
print(worst_day)
