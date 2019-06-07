import os
import csv

# Path to collect data from the Resources folder

wrestling_csv = os.path.join('..', 'Class3', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter

def print_percentages(wrestler_data):
    name=wrestler_data[0]
    wins=int(wrestler_data[1])
    losses=int(wrestler_data[2])
    draws=int(wrestler_data[3])
# Find the total number of matches wrestled
    totalmatches = wins+losses+draws
# Find the percentage of matches won
    
    winpercent=wins/totalmatches
# Find the percentage of matches lost
    
    losspercent=losses/totalmatches

# Print out the wrestler's name and their percentage stats

    print(
        f"The wrestler {name} has {wins} wins, {losses} losses, and {draws} draws. Their win percent is {winpercent} and loss percent is {losspercent}."
        )
    if winpercent > 0.5:
        print(f"{name} is a Superstar")
    else:
        print(f"{name} is a Jobber")

#~~~~~
# Prompt the user for what wrestler they would like to search for
name_to_check = input("What wrestler do you want to look for? ")

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')



    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
