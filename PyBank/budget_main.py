#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import csv

csvpath = 'budget_data.csv'

month_counter = 0 
profits_losses = 0
previous_profit = 0

changes = []
month_for_change = {}

with open(csvpath, 'r') as csvfile:  
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)
	for row in csvreader:
		month_counter += 1
		profits_losses = profits_losses + int(row[1])
		change = int(row[1]) - int(previous_profit)
		changes.append(change)
		previous_profit = row[1]
		month_for_change[change]=row[0]
changes=changes[1:]	
average=sum(changes)/len(changes)
average=str(round (average,2))	
max_changes = max(changes)
min_changes = min(changes)

print("Financial Analysis")
print("Total Months: " + str(month_counter))
print("Total Net Amount: $" + str(profits_losses))
print("Average Change: $" + str(average))
print("Greatest Increase in profits: " + str(month_for_change[max_changes]) + " ($" +str(max_changes) +")") 
print("Greatest Decrease in profits: " + str(month_for_change[min_changes]) + " ($" +str(min_changes) +")") 

with open("analysis_bank.txt", 'w') as f:
	f.write = ("Financial Analysis")
	f.write = ("Total Months: " + str(month_counter))
	f.write = ("Total Net Amount: $" + str(profits_losses))
	f.write = ("Average Change: $" + str(average))
	f.write = ("Greatest Increase in profits: " + str(month_for_change[max_changes]) + " ($" +str(max_changes) +")") 
	f.write = ("Greatest Decrease in profits: " + str(month_for_change[min_changes]) + " ($" +str(min_changes) +")") 


	







