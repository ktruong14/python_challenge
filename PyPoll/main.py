# Importing os and reading CSV module
import os
import csv

election_csv = os.path.join('PyPoll','Resources','election_data.csv')

voters = []
candidates = []

with open(election_csv,'r') as csvfile:
    
    csv_reader = csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)

    # Declaring variables
    
    for row in csv_reader:
        voters.append(int(row[0]))
        candidates.append(str(row[2]))
    
no_of_voters = len(voters)
khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0

    # For loop to count number of votes per candidates
for row in candidates:
        
    if row == "Khan":        
        khan_count = khan_count + 1
    elif row == "Correy":
        correy_count = correy_count + 1
    elif row == "Li": 
        li_count = li_count + 1
    else:
        tooley_count  = tooley_count + 1

    if khan_count > correy_count:
        winner = "Khan"
    elif khan_count > li_count:
        winner = "Khan"
    elif khan_count > tooley_count:
        winner = "Khan"
    elif correy_count > li_count:
        winner = "Correy"
    elif correy_count > khan_count:
        winner = "Correy"
    elif correy_count > tooley_count:
        winner = "Correy"
    elif tooley_count > khan_count:
        winner = "O'Tooley"
    elif tooley_count > li_count:
        winner = "O'Tooley" 
    elif tooley_count > correy_count:
        winner = "O'Tooley"
    
    khan_percent = (khan_count/no_of_voters) * 100
    correy_percent = (correy_count/no_of_voters) * 100
    li_percent = (li_count/no_of_voters) * 100
    tooley_percent = (tooley_count/no_of_voters) * 100
    
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(no_of_voters))
    print("-----------------------")
    print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_count) + ")")
    print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_count) + ")")
    print("Li: " + str(li_percent) + "% " + "(" + str(li_count) + ")")
    print("O'Tooley: " + str(tooley_percent) + "% " + "(" + str(tooley_count) + ")")
    print("-----------------------")
    print("Winner: " + winner)
    print("-----------------------")

# Exporting results to txt
output = os.path.join("PyPoll","analysis","output.txt")

with open(output, 'w') as textfile:
    textfile.write("Election Results")
    textfile.write("\n-----------------------")
    textfile.write("\nTotal Votes: " + str(no_of_voters))
    textfile.write("\n-----------------------")
    textfile.write("\nKhan: " + str(khan_percent) + "% " + "(" + str(khan_count) + ")")
    textfile.write("\nCorrey: " + str(correy_percent) + "% " + "(" + str(correy_count) + ")")
    textfile.write("\nLi: " + str(li_percent) + "% " + "(" + str(li_count) + ")")
    textfile.write("\nO'Tooley: " + str(tooley_percent) + "% " + "(" + str(tooley_count) + ")")
    textfile.write("\n-----------------------")
    textfile.write("\nWinner: " + winner)
    textfile.write("\n-----------------------")
