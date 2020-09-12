# Importing os and reading CSV module
import os
import csv

budget_csv = os.path.join('PyBank','Resources','budget_data.csv')
# Reading CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    # Declaring variables and calculations
    date = []
    profit_loss = []
    for row in csvreader:
        profit_loss.append(int(row[1]))  
        date.append(row[0])

    increase_profits = max(profit_loss)
    decrease_profits = min(profit_loss)
    total_months = len(date)
    net_total = sum(profit_loss)
    avg_change = int(net_total) / int(total_months)
    increase_profits_index = profit_loss.index(increase_profits) 
    decrease_profits_index = profit_loss.index(decrease_profits)
    increase_profits_date = date[increase_profits_index]
    decrease_profits_date = date[decrease_profits_index]
    
    # Printing output
    print("Financial Analysis")
    print("---------------------------" )
    print("Total Months: " + str(total_months))
    print("Total: $" + str(net_total))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase in Profits: " + str(increase_profits_date) + " " + "(" + str(increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_profits_date) + " " + "(" + str(decrease_profits) + ")")

# Exporting results to txt
output = os.path.join("PyBank","analysis","output.txt")
with open(output, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------\n")
    textfile.write("Total Months: " + str(total_months))
    textfile.write("\nTotal: $" + str(net_total))
    textfile.write("\nAverage Change: " + str(avg_change))
    textfile.write("\nGreatest Increase in Profits: " + str(increase_profits_date) + " " + "(" + str(increase_profits) + ")")
    textfile.write("\nGreatest Decrease in Profits: " + str(decrease_profits_date) + " " + "(" + str(decrease_profits) + ")")

