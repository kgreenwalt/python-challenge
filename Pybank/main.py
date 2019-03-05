import os
import csv

# Path to collect data from the Resources folder
budget_path = os.path.join("PyBank","Resources","budget_data.csv")

# Create empty lists for month and revenue data
months = []
revenue = []
revenue_change_list = []

# Create variables and set initial values
total_revenue = 0
previous_revenue = 0
revenue_change = 0
max_increase = 0
max_decrease = 0

#Open and read csv, skipping header
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

# Add data to months and revenue lists
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
# Find total months
total_months = len(months)

# Build out revenue change list
revenue_change = int(row[1]) - previous_revenue
revenue_change_list.append(revenue_change)

# Print analysis
print("Financial Analysis")

print(f"Total Months:{str(total_months)}")
print(f"Total:{str(total_revenue)}")
print(f"Average Change:{str(revenue_change)}")
#print(f"Greatest Increase in Profits:{str(")






