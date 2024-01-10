import csv

file_path = "budget_data.csv"

total_months = 0
net_total = 0
prev_profit_loss = 0
changes = []
dates = []

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        net_total += profit_loss
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            changes.append(change)
            dates.append(date)

        prev_profit_loss = profit_loss

average_change = round(sum(changes) / len(changes), 2)
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file_path = "financial_analysis_results.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-" * 30 + "\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Results exported to {output_file_path}")


"""
Created on Tue Jan  9 20:41:10 2024

@author: Walter Hampson
"""

