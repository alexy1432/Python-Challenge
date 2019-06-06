import os
import csv
date = []
revenue =[]
RevenueChange2 =[]
TotalRevenue =0
StartingRevenue=0
itemCount = 0
AverageRevenueChange = 0
TotalRevenueChange = 0 
csvpath = os.path.join("..", "PyBank", "budget_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #counts the row total and stores the dates
            itemCount = itemCount + 1
            date.append(row[0])
        #calculates the total revenue
            revenue.append(int(row[1]))
            TotalRevenue = sum(revenue)
        #calculates the change in revenue per row
            EndingRevenue = int(row[1])
            RevenueChange = EndingRevenue - StartingRevenue
            RevenueChange2.append(RevenueChange)
            StartingRevenue = EndingRevenue
        #creates a list of the change in revenue per row in order to call the total, average, min and max values
            Greatest = int(max(RevenueChange2))
            Least = int(min(RevenueChange2))
                       
#calls the row value for the greatest and least changes in revenue        
GreatestDate = date[RevenueChange2.index(Greatest)]
LeastDate = date[RevenueChange2.index(Least)]
RevenueChange2.pop(0)
TotalRevenueChange = sum(RevenueChange2)
AverageRevenueChange = TotalRevenueChange/(itemCount-1) 

    
with open("calculations" + '.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------" + "\n")
    text.write("Total Months: " + str(itemCount) + "\n")
    text.write("Total: " + "$" + str(TotalRevenue) + "\n")
    text.write("Average Change: " + "$" + str(AverageRevenueChange) + "\n")
    text.write("Greatest Increase in Profits: " + str(GreatestDate) + " " + "(" + "$" + str(Greatest) + ")" + "\n")
    text.write("Greatest Increase in Profits: " + str(LeastDate) + " " + "(" + "$" + str(Least) + ")" + "\n")



            
            