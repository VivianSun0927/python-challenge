import os
import csv
from pathlib import Path 

#pathing to the csv file for PyBank data
csvpath = os.path.join("Resources", "budget_data.csv")

#set variables
total_months = []
total_profits = []
monthly_profit_changes = []



#read file contents
with open(csvpath, newline="", encoding="utf-8") as read:
  csv_read = csv.reader(read, delimiter=",")

  header = next(csv_read)

#define rows from csv for total months and profits/losses
  for row in csv_read:
    total_months.append(row[0])
    total_profits.append(int(row[1]))

#changes to profit/losses and append monthly profit changes
  for i in range(len(total_profits)-1):
    monthly_profit_changes.append(total_profits[i+1]-total_profits[i])

#determine the highest and lowest of profit change
max_increase = max(monthly_profit_changes)
max_decrease = min(monthly_profit_changes)

#determine the months that are associated with the highest and lowest changes in profits
max_increase_month = monthly_profit_changes.index(max(monthly_profit_changes)) + 1
max_decrease_month = monthly_profit_changes.index(min(monthly_profit_changes)) + 1 

#print analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profits)}")
print(f"Average Change: {round(sum(monthly_profit_changes)/len(monthly_profit_changes),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

# Export text files
output_file = Path("analysis", "Financial_Analysis.txt")

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profits)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_changes)/len(monthly_profit_changes),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")