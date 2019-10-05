import os
import csv

filepath = 'Resources/budget_data.csv'

date = []
profit = []

with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)
    for row in reader:
        date.append(row[0])
        profit.append(int(row[1]))

months = []
years = []

month_count = len(date)
net_profit = sum(profit)
average_profit = round(net_profit/month_count, 2)

max_profit = max(profit)
max_date = date[profit.index(max(profit))]

max_loss= min(profit)
min_date = date[profit.index(min(profit))]

output = 'Resources/output.csv'

with open(output, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Financial Analysis'])
    writer.writerow(['----------------------------'])
    writer.writerow([f'Total Months: {month_count}'])
    writer.writerow([f'Total: ${net_profit}'])
    writer.writerow([f'Average Change: ${average_profit}'])
    writer.writerow([f'Greatest Increase In Profits: {max_date} (${max_profit})'])
    writer.writerow([f'Greatest Decrease In Profits: {min_date} (${max_loss})'])

print('Financial Analysis\n----------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${net_profit}')
print(f'Average Change: ${average_profit}')
print(f'Greatest Increase In Profits: {max_date} (${max_profit})')
print(f'Greatest Decrease In Profits: {min_date} (${max_loss})')
