#!/usr/bin/env python
# coding: utf-8

# In[264]:


# final Result should be: as below

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# ------------------------------------------------------


# define dependency

import os
import csv

# file to load and output

file_to_load = os.path.join(".", "Resources", "budget_data.csv")
# print(file_to_load)

file_to_output = os.path.join(".", "financial_analysis.txt")
# print(file_to_output)

total_months = 1
total = 0

# average_change = 0
increase_profit = 0
decrease_profit = 0

net_change_list =[]
month =[]

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # print(reader)

  
    header = next(reader)
    # print(f"Header:{header}")

    first_row = next(reader)
    # print(first_row)
    total = total + int(first_row[1]) #1088983
    prv_total = int(first_row[1]) #1088983
    
    for row in reader:
        
        # to get the total
        total_months = total_months + 1
        # print(total_months)
        total = total + int(row[1])

        month.append(row[0])
        # print(month)
        
        # to get average change
        net_change = int(row[1]) - prv_total
        prv_total = int(row[1])
        net_change_list.append(net_change)
        # print(net_change_list)
        
        # to get greatest increase & greatest decrease
        increase_profit = max(net_change_list)
        decrease_profit = min(net_change_list)

        # to get highest increse profit month & lowest decrease profit month
        increse_profit_month = net_change_list.index(increase_profit)
        decrease_profit_month = net_change_list.index(decrease_profit)

        highest_profit_month = month[increse_profit_month]
        lowest_profit_month = month[decrease_profit_month]


average_change = sum(net_change_list)/ len(net_change_list)

# final result
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change:{average_change:.2f}\n"
    f"Greatest Increase in Profits: {highest_profit_month} (${increase_profit}) \n"
    f"Greatest Decrease in Profits: {lowest_profit_month} (${decrease_profit}) \n"
    f"------------------------------------------------------\n"
)
print(output)

#to write final result in text file
with open(file_to_output, "w") as text_file:
    text_file.write(output)


# In[ ]:




