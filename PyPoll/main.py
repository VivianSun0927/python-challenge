import os
import csv
from pathlib import Path 

#pathing to the csv file for PyPoll data
csvpath = Path("Resources", "election_data.csv")

#set variables
total_votes = 0 
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

#read file contents and store data
with open(csvpath,newline="", encoding="utf-8") as read:
  csv_read = csv.reader(read, delimiter=",")

  header = next(csv_read)

  for row in csv_read:
    #counting total voter IDs
      total_votes += 1
    #count number of times each candidate make an appearance down the list
      if row[2] == "Charles Casper Stockham":
        Charles_votes +=1
      elif row[2] == "Diana DeGette":
        Diana_votes +=1
      elif row[2] == "Raymon Anthony Doane":
        Raymon_votes +=1

#create a dictionary for the candidate names as well as variables
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_votes, Diana_votes, Raymon_votes]

#zip the candidates and total votes together, then determine winners utilizing max values within the dictionary created
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#find the percentage values of total votes per candidate
Charles_percent = (Charles_votes/total_votes) *100
Diana_percent = (Diana_votes/total_votes) * 100
Raymon_percent = (Raymon_votes/total_votes)* 100

#print analysis results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Export text files
output_file = Path("analysis", "Election_Results.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")