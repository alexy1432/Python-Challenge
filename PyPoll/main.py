import os
import csv
csvpath = os.path.join("..", "PyPoll", "Resources_election_data.csv")
itemCount = 0
candidates = []
ucandidates = []
counter = 0
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
    print(ucandidates)
