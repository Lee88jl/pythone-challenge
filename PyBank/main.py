#Modules
import os
import csv

#Set path for file
csvpath = os.path.join("..", "PyBank\Resources", "budget_data.csv")

# Open CSV file
with open(csvpath, encoding='utf') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

# Skip the header row
    next(reader)

# Initializing value to store sum
    diff_values = []
    profit = []
    date = []
    
    count = 0
    total = 0
    initial = 0

    first_row = next(reader)
    prev_value = int(first_row[1])
    total = prev_value
  
# Calculating total months
    for row in reader:
        count = count +1

        row_count = reader.line_num - 1 

# Calculate dollar total
        profit.append(row[1])
        total = total + int(row[1])

# Calculating Changing Average
        curr_value = int(row[1])
        diff = curr_value - prev_value
        diff_values.append(diff)
        prev_value = curr_value

# List and add the difference for Loop
# Keeps track of actual months
        date.append(row[0])        
        max_diff = max(diff_values)
        min_diff = min(diff_values)
        max_date = date[diff_values.index(max_diff)]
        min_date = date[diff_values.index(min_diff)]

# calculate difference outside for loop 
average = round((sum(diff_values) / int(count)), 2)

# Print the outcome
print("Financial Analysis")
print("-----------------------------------------")
print ("Total Months:", row_count)
print (f"Total: ${total}")
print (f"Average Change: ${average}")
print (f"Greatest Increase in Profits: {str(max_date)} (${max_diff})")
print (f"Greatest Decrease in Profits: {str(min_date)} (${min_diff})")

# Write the Outcome as text
output = os.path.join ("Analysis.txt")
with open(output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------------------\n")
    file.write (f"Total Months: {row_count}\n")
    file.write (f"Total: ${total}\n")
    file.write (f"Average Change: ${average}\n")
    file.write (f"Greatest Increase in Profits: {str(max_date)} (${max_diff})\n")
    file.write (f"Greatest Decrease in Profits: {str(min_date)} (${min_diff})\n")
    file.close()
    pass