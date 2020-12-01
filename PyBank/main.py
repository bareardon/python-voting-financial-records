import os
import csv

# Path to collect data from the Resources folder
budget_csv_path = os.path.join('Resources', 'budget_data.csv')

# Define variables
total_months = 0
net_total = 0

# Read in the CSV file
with open(budget_csv_path) as csvfile: 

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimeter=',')

    header = next(csvreader)

# Loop through the rows of data
    for row in csvreader:

# Calcuate the total number of months in the dataset
    total_months = total_months + 1

# Calculate the net total amount of Profits/Losses over the entire period
    net_total = net_total + int(row[1])

# Set format for printing
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {}\n"
    f"Total: $ {}\n"
    f"Average Change: $ {}\n"
    f"Greatest Increase in Profits:  {}{}\n"
    f"Greatest Decreatse in Losses:  {}{}"
)


with open("analysis/output.txt", "w") as txt_file: 
    txt_file.write(output)
