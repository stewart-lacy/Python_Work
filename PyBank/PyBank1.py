import os 
import csv 

file_to_load = "Resources/budget_data.csv"

total_month = 0 
net_total = 0
change_months = []
change_value = []
rev_list = []
greatest_increase = ["", 0]
greatest_decrease = ["",0]
with open(file_to_load) as pybank_data:
    reader = csv.DictReader(pybank_data)
    first_row = next(reader)
    total_month = total_month + 1
    last_rev_change = int(first_row["Profit/Losses"])
    net_total =  net_total + int(first_row["Profit/Losses"])
    

    for row in reader: 
        #Number of total months
        total_month = total_month + 1
        net_total += int(row["Profit/Losses"])

        #The average of the changes in "Profit/Losses" over the entire period
        #Question:how to show only two decimals 
        rev_change = int(row["Profit/Losses"]) - last_rev_change
        last_rev_change = int(row["Profit/Losses"])
        rev_list = rev_list + [rev_change]
        change_months = change_months + [row["Date"]]
        avg_rev_change = (sum(rev_list) / len(rev_list))

        #greatest increase 
        if rev_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = rev_change

        if rev_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = rev_change


answer = (
    f"\n Financial Analysis\n"
    f" ----------------------------\n"
    f"\nTotal Months: {total_month}\n"
    f"\nTotal : ${net_total}\n"
    f"\nAverage Change : ${avg_rev_change:.2f}\n"
    f"\nGreatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"\nGreatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}\n")  
print(answer)  
output_file = os.path.join("PyBankSolved.txt")
with open(output_file, "w", newline="") as txt_file:
    txt_file.write(answer)
