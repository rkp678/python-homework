# Homework 2 - Rachel Pierce

# # Calculate the following:
# The total number of months included in the dataset.
# The net total amount of Profit/Losses over the entire period.
# The average of the changes in Profit/Losses over the entire period.
# The greatest increase in profits (date and amount) over the entire period.
# The greatest decrease in losses (date and amount) over the entire period.

# %%

import csv
filepath = "C:/Users/piercerachel/Desktop/git/python-homework/budget_data.csv"

records = []
months = 0
net_profit = 0
month_chg = 0
avg_chg = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]
net_chg_list = []

# %%

# Calculate the total number of months included in the dataset.

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)


    for row in csvreader:
        print(row)
        
        date = row[0]
        profit_loss = int(row[1])
        months = months + 1      
        print(months)
        
# Answer: Total number of months is 86   
     
# %%

# Calculate the net total amount of Profit/Losses over the entire period.
 
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)
     
    for row in csvreader:
        print(row)
        
        date = row[0]
        profit_loss = int(row[1])
        net_profit = net_profit + profit_loss     
        print(net_profit)
    
# Answer: Total net profit is 38382578
    
# %%

# The average of the changes in Profit/Losses over the entire period.
# The greatest decrease in losses (date and amount) over the entire period.
# The greatest decrease in losses (date and amount) over the entire period.

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    csv_header = next(csvreader)
    print(csv_header)
    prev_mth = int(csv_header[1]) 
    for row in csvreader:
        print(row)
        
        date = row[0]
       
        # profit_loss = int(row[1])
        net_chg = int(row[1]) - prev_mth
        prev_mth = int(row[1])
        net_chg_list = net_chg_list + [net_chg]
        
        if net_chg > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_chg
        
        if net_chg < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_chg
        
    sum_net_chg = sum(net_chg_list)
    month_size = len(net_chg_list)
    print(sum_net_chg/month_size)
    print(greatest_increase)
    print(greatest_decrease)
    

# Answer: Average change is -2315.12
# Answer: Greatest Increase in profits is from February 2012 of 1926159
# Answer: Greatest Decrease in profits is from September 2013 of -2196167

# %%

# Resulting Analysis:
    
# Financial Analysis
# ------------------------
print("Total Months: ",months)

print("Total: $",net_profit)

print("Average Change: $",round(sum_net_chg/month_size,2))

print("Greatest Increase in Profits: ",greatest_increase)

print("Greatest Decrease in Profits: ",greatest_decrease)




