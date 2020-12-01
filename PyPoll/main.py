import os
import csv

# Path to collect data from Resources folder
election_csv_path = os.path.join('Recources', 'election_data.csv')

# Define Variables 
total_votes = 0 

winner = {'candidate': 2}

# Read is csv file
with open(election_csv_path) as csvfile

    # Split the data on commas 
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the rows of data 
    for row in csvreader:

        # Calculate the total number of votes cast 
        total_votes = total_votes + 1

        # Generate a list of candidates who recevied votes

        # Calculate the percentage of votes each candidate won
        total_votes = 
        
        # Calculate the total number of votes each candidate won
        if 

        # Determine the winner of the election based on the poplar
        # use max function to see who received most votes 

# Set format for printing 
output = (
    f"Election Results\n"
    f"-----------------\n"
    f"Total Votes {}\n"
    f"-----------------\n"

     f"-----------------\n"
     f"Winner {}\n"


)

with open("analysis/output.txt", "w") as txt_file: 
    txt_file.write(output)