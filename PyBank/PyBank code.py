import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, encoding = "utf") as x:
    csvreader = csv.reader(x, delimiter =",")

    next(csvreader, None)

    # create lists 
    months = []
    profits = []
    profit_changes = []

    for row in csvreader: 
     # append months and profits to the created lists 
        months.append(row[0])
        profits.append(int(row[1]))


    # iterate through all profits to get profit changes 
for i in range(len(profits)-1):
        
        # find the profit change between index i and index i + 1 and then append to profit change list  
    profit_changes.append(profits[i+1]-profits[i])
        
# find the max and  min of profit changes in loop above 
max_increase = max(profit_changes)
max_decrease = min(profit_changes)

# find the index for the month of the max increase and decrease 
max_increase_month = profit_changes.index(max(profit_changes)) + 1
max_decrease_month = profit_changes.index(min(profit_changes)) + 1 
 
# calculation for average change for summary 
avg_change = round(sum(profit_changes)/len(profit_changes),2)

# output file, using f string 
output_analysis = (f"Fianacial Analysis\n----------------------------\nTotal Months: {len(months)}\nTotal: ${sum(profits)}\nAverage Change: {avg_change}\nGreatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase))})\nGreatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease))})")
with open('outputfile.txt', 'w') as output:
    output.write(output_analysis)
# using 'w' creates a new textfile 
print(output_analysis)

