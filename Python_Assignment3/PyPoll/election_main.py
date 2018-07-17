#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
# hint: dictionary of votes per person
#import os
import csv 

csvpath = 'election_data.csv'

total_votes = 0
candidates_list=[]
votes_per_person={}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        total_votes += 1
        candidates = row[2]
        if candidates not in candidates_list:
            candidates_list.append(candidates) 
        if candidates not in votes_per_person: 
            votes_per_person[candidates] = 0   
        votes_per_person[candidates] += 1 

print("PyPoll Results:")
print("Total votes: " + str(total_votes))

winnner= None
most_votes=0

for name, number_votes in votes_per_person.items():
    print("{} : {:.2f}% votes ({})".format(name,number_votes/total_votes*100, number_votes))
    if number_votes> most_votes:
        winner = name
        most_votes =number_votes
print("Winner: {} ".format(winner))        
#print(votes_per_person)        


with open ("analysis.txt", "w") as f:
    f.write("""PyPoll Results
    """)

    f.write("""Total votes: """ + str(total_votes))

    for name, number_votes in votes_per_person.items():      
        f.write("""  
        {} : {:.2f}%  ({})\n""".format(name,number_votes/total_votes, number_votes))
        if number_votes> most_votes:
            winner=name
            most_votes =number_votes
    f.write("WINNER: {} ".format(winner))



   


