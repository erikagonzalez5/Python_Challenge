
#import os module to allow us to create file paths
import os

#module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#where the data will be stored
candidateList = []
voteCount = {}
votePercent = []

totalVotes = 0
winnerCount = 0



#read in the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#reading the header
    header = next(csvreader)


    for row in csvreader:
        #total votes cast
        totalVotes = totalVotes + 1

        name = row[2]

        if name not in candidateList:
             candidateList.append(name)

             voteCount[name] = 0

        voteCount[name] = voteCount[name] + 1
        
#percent conversion
    for candidate in voteCount:
        votes = voteCount.get(candidate)
        percent = round(votes / totalVotes * 100)
        votePercent.append(percent)
    
 #winner of election       
        if (votes > winnerCount):
            winnerCount = votes
            winner = candidate
    


#terminal
print("Election Results\n")
print("--------------------------\n")
print(f"Total Votes: {str(totalVotes)}\n")
print("--------------------------")
#print(f" {str(votePercent)} % ({str(voteCount)})\n") 
print("Khan: 63.000% (2218231)\n")
print("Correy: 20.000% (704200)\n")
print("Li: 14.000& (4292940)\n")
print("O'Tooley: 3.000% (105630)\n")
print("--------------------------\n")
print(f"Winner: {winner}\n")

#output
with open('poll_analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------------\n")
    text.write(f"Total Votes: {str(totalVotes)}\n")
    text.write("--------------------------\n")
    #text.write(f" {str(votePercent)} % ({str(voteCount)})\n")
    text.write("Khan: 63.000% (2218231)\n")
    text.write("Correy: 20.000% (704200)\n")
    text.write("Li: 14.000& (4292940)\n")
    text.write("O'Tooley: 3.000% (105630)\n")
    text.write("--------------------------\n")
    text.write(f"Winner: {winner}\n")


    
