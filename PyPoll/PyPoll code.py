import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path, encoding = "utf") as x:
    csvreader = csv.reader(x, delimiter =",")

    next(csvreader, None)

    # create variables for votes 
    total_votes = 0 
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0

    # iterate through the data add one vote per row 
    for row in csvreader:
        total_votes +=1

        # add 1 vote that each candidate receives 
        if row[2] == "Charles Casper Stockham": 
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1

# create a dictionary with the candidate and total votes   
votecount_dict = {"Charles Casper Stockham": stockham_votes, "Diana Degette": degette_votes, "Raymon Anthony Doane": doane_votes}
# find the winner by comparing the total votes
winner = max(votecount_dict, key = votecount_dict.get)

# Print a the summary of the analysis
stockham_voteshare = (stockham_votes/total_votes) *100
degette_voteshare = (degette_votes/total_votes) * 100
doane_voteshare = (doane_votes/total_votes)* 100

# output file 
output_analysis = (f"Election Results\n----------------------------\n Total Votes: {total_votes}\n----------------------------\n Charles Casper Stockham: {stockham_voteshare:.3f}% ({stockham_votes})\n Diana Degette: {degette_voteshare:.3f}% ({degette_votes})\n Raymon Anthony Doane: {doane_voteshare:.3f}% ({doane_votes})\n ----------------------------\n Winner: {winner}\n ----------------------------")
with open('outputfile.txt', 'w') as output:
    output.write(output_analysis)

print(output_analysis)