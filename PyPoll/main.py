import os
import csv
csvpath = os.path.join("..", "PyPoll", "Resources_election_data.csv")
itemCount = 0
candidates = []
ucandidates = []
VoteCount = []
VoteCountPercent = []
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
#calculates total number of votes
        itemCount = itemCount + 1
#creates list of unique candidate names    
        candidates.append(row[2])
    for x in candidates: 
        if x not in ucandidates:  
            ucandidates.append(x)
#calls the count of each vote per candidate and stores into a list 
            count = candidates.count(x)
            VoteCount.append(count)
            VoteCountPercent.append(candidates.count(x)/itemCount)
#assign a winner by taking the index value of the candidate with the highest votes
    Winner = ucandidates[VoteCount.index(max(VoteCount))]

with open("Election Results" + ".txt", "w") as text:      
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write("Total Votes: " + str(itemCount) + "\n")
    text.write("-------------------------" + "\n")
    text.write(ucandidates[0] + ": " + str(round((VoteCountPercent[0])*100,1)) + "% " + "(" + str(VoteCount[0]) + ")" + "\n")         
    text.write(ucandidates[1] + ": " + str(round((VoteCountPercent[1])*100,1)) + "% " + "(" + str(VoteCount[1]) + ")" + "\n")
    text.write(ucandidates[2] + ": " + str(round((VoteCountPercent[2])*100,1)) + "% " + "(" + str(VoteCount[2]) + ")" + "\n")
    text.write(ucandidates[3] + ": " + str(round((VoteCountPercent[3])*100,1)) + "% " + "(" + str(VoteCount[3]) + ")" + "\n")
    text.write("-------------------------" + "\n")
    text.write("Winner: " + str(Winner) + "\n")
    text.write("-------------------------" + "\n")