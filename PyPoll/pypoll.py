#!/usr/bin/env python
# coding: utf-8

# In[126]:


# final Result should be: as below

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

import os
import csv

# file to load and output

file_to_load = os.path.join(".", "Resources", "election_data.csv")
#print(file_to_load)

file_to_output = os.path.join(".", "election_analysis.txt")
#print(file_to_output)

total_vote = 0
candidate_vote = {}
candidate_option = []

winning_count = 0

with open (file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    # print(f"Header: {header}")

    # first_row = next(reader)
    # print(first_row)
    
    for row in(reader):
        
        total_vote = total_vote + 1

        candidate_name = (row[2])

        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            
            candidate_vote[candidate_name] = 0
        candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1

output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"-------------------------"
    )
     
with open (file_to_output, "w") as text_file:
    text_file.write(output)
    print(output)
    
    for candidate in candidate_vote:
        
        votes = candidate_vote[candidate]
        persentage_vote = float(votes)/ float(total_vote) * 100
        
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voting_result = f"{candidate}: { persentage_vote:.3f}% ({votes})\n"
        print(voting_result, end="")
        text_file.write(voting_result)
        
    final_winner = (f"-------------------------\n"
    f"Winner: {winning_candidate} \n"
    f"-------------------------\n"   
     )
    print(final_winner)
    text_file.write(final_winner)
    



# In[ ]:





# In[ ]:




