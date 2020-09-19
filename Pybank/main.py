#import libraries
import pandas as pd
import numpy as np
from pathlib import Path

#import csv file and define it


file_path = Path("Resources/budget_data.csv")

budget_data = pd.read_csv(file_path)

#create a dictionary with the dates
dates = budget_data['Date']
PnL = budget_data['Profit/Losses']
total_info = dict(zip(dates, PnL))

#define variables
total_num_months = 0
net_total_PnL = 0
average_change_PnL = 0
greatest_increase_profits = 0 
greatest_decrease_profits = 0
max_date = []
min_date = []

#set values for variables
num_months = len(PnL)

#net_total
for x in PnL:
   net_total_PnL = net_total_Pnl + x

#average
average_change_PnL = round(net_total_PnL / num_months, 2)

maximum = PnL.max()

minimum = PnL.min()

max_date = list(total_info.keys())[list(total_info.values()).index(1170593)]

min_date = list(total_info.keys())[list(total_info.values()).index(-1196225)]

# Set output file name
output_path = 'output.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    # Write daily_average to the output file, convert to string
    file.write(f"Financial Analysis\n")
    file.write(f"-------------------------------")
    file.write(f"Total Months: {num_months}")
    file.write(f"Total {net_total_PnL}.")
    file.write(f"Average Change : ${average_change_PnL} ")
    file.write(f"Greatest Increase in Profits {max_date} , {maximum}")
    file.write(f"Greatest Decrease in Profits {min_date} , {minimum} ")