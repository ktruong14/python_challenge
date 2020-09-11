# Importing os and reading CSV module
import os
import csv

budget_csv = os.path.join('PyBank','Resources','budget_data.csv')

def analysis(budget_csv):
    
    month_name = str(budget_csv[0])
    months = int(budget_csv[0])
    profit_loss = int(budget_csv[1])

    total_months = len(months)
    net_total = sum(profit_loss)
    avg_change = net_total / total_months
    increase_profits = int(budget_csv[1].max())
    decrease_profits = int(budget_csv[1].min())
    
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + total_months)
    print("Total: $" + net_total)
    print("Average Change: " + avg_change)
    print("Greatest Increase in Profits: " + increase_profits)
    print("Greatest Decrease in Profits: " + decrease_profits)

# Reading CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through data
    for row in csvreader:
        if month_name == row[0]

# Exporting to a txt file

