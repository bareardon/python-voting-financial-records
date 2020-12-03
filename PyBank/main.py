import os
import csv

# Path to collect data from the Resources folder
budget_csv_path = os.path.join('Resources', 'budget_data.csv')

# Define variables
total_months = 0
net_total = 0
monthly_change = []
previous_value = 0 
average_change = 0
greatest_increase = {'month': '', 'value': 0}
greatest_decrease = {'month': '', 'value': 0}

# Read in the CSV file
with open(budget_csv_path) as csvfile: 

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the rows of data 
    for row in csvreader:

        #Calcuate the total number of months in the dataset
        total_months = total_months + 1

        #Calculate the net total amount of Profits/Losses over the entire period
        net_total = net_total + int(row[1])

        #Calculate the changes in Profits/Losses over the entire period
        profit_change = int(row[1]) - previous_value 
        monthly_change.append(profit_change)
        previous_value = int(row[1])

        #Greatest increase in profits (date & amount) over entire period
        if greatest_increase['value'] < int(row[1]):
            greatest_increase['month'] = row[0]
            greatest_increase['value'] = int(row[1])


        #Greatest decrease in losses (date and amount) over the entire period
        if greatest_decrease['value'] > int(row[1]):
            greatest_decrease['month'] = row[0]
            greatest_decrease['value'] = int(row[1])

    #Calculate the average change of profits/losses
    average_change = sum(monthly_change) / total_months



# Set format for printing
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: $ {round(average_change,2)}\n"
    f"Greatest Increase in Profits:  {greatest_increase['month']}  (${greatest_increase['value']})\n"
    f"Greatest Decrease in Losses:   {greatest_decrease['month']}  (${greatest_decrease['value']})\n"
)


with open("analysis/output.txt", "w") as txt_file: 
    txt_file.write(output)
