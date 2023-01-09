import os
import csv

# Import csv
csvpath = os.path.join("..", "PyPoll\Resources", "election_data.csv")

# Open CSV file
with open(csvpath, encoding='utf') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

# Skip the header row
    next(reader)

# Initialize a counter variable
    row_count = 0
    count_C = 0
    count_D = 0
    count_R = 0
    frequency = {}

# Calculate total votes
    for row in reader:
        row_count += 1

# Calculate each candidate votes
        if row[2] == 'Charles Casper Stockham':
            count_C += 1

        if row[2] == 'Diana DeGette':
            count_D += 1

        if row[2] == 'Raymon Anthony Doane':
            count_R += 1

# Calculate percentage of votes
percentage_C = '{:.3%}'.format(count_C / row_count)
percentage_D = '{:.3%}'.format(count_D / row_count)
percentage_R = '{:.3%}'.format(count_R / row_count)

# Find the winner of the election
# Create a dictionary with the candidates
Result = {"Charles Casper Stockham":count_C, "Diana DeGette":count_D, "Raymon Anthony Doane":count_R}
Winner = max(Result, key=Result.get)

#Print all the values
print ("Election Results")
print("-----------------------------------------")

print("Total Votes:", row_count)

print("-----------------------------------------")

print(f"Charles Casper Stockham: {percentage_C} ({count_C})")
print(f"Diana DeGette: {percentage_D} ({count_D})")
print(f"Raymon Anthony Doane: {percentage_R} ({count_R})")

print("-----------------------------------------")

print ("Winner: ", Winner)

print("-----------------------------------------")

# Write outcome to text file
output = os.path.join ("Analysis.txt")
with open(output, 'w') as file:
    file.write ("Election Results\n")
    file.write("-----------------------------------------\n")
    file.write(f"Total Votes: {row_count}\n")
    file.write("-----------------------------------------\n")
    file.write(f"Charles Casper Stockham: {percentage_C} ({count_C})\n")
    file.write(f"Diana DeGette: {percentage_D} ({count_D})\n")
    file.write(f"Raymon Anthony Doane: {percentage_R} ({count_R})\n")
    file.write("-----------------------------------------\n")
    file.write (f"Winner: {Winner}\n")
    file.write("-----------------------------------------\n")