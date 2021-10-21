#import os module to allow us to create file paths
import os

#module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#where the data will be stored
monthChanges = []
revenue = []
date = []


monthCount = 0
totalRevenue = 0
profitLossChange = 0
greatestIncrease = 0
greatestMonthI = 0
greatestMonthD = 0
greatestDecrease = 0
initialProfit = 0


#read in the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#reading the header
    header = next(csvreader)


    for row in csvreader:
        date.append(row[0])
#month count
        monthCount = monthCount + 1

#need to append the profit info and calculate the total revenue
        revenue.append(row[1])
        totalRevenue = totalRevenue +int(row[1])

#calculate changes and average in profits
        profitLossChange = int(row[1]) - initialProfit
        monthChanges.append(profitLossChange)
        initialProfit = int(row[1])

        #revenueChangeList = revenueChangeList + [revenueChange]

        # monthChanges = monthChanges + [row[0]]

        if int(row[1]) > greatestIncrease:
                greatestIncrease = int(row[1])
                greatestMonthI = row[0]
        
        if int(row[1]) < greatestIncrease:
                greatestDecrease = int(row[1])
                greatestMonthD = row[0]


        averageChanges = sum(monthChanges) / len(monthChanges)

#finding maximimum and minimum changes in profits
        greatestIncrease = max(monthChanges)
        greatestDecrease = min(monthChanges)



#terminal
    print("----------------------------------------------------------\n")
    print("Financial Analysis")
    print("----------------------------------------------------------\n")
    print("Total Months: " + str(monthCount))
    print("Total Profits: " + "$" + str(totalRevenue))
    print("Average Change: " + "$" + str(int(averageChanges)))
    print("Greatest Increase in Profits: " + str(greatestMonthI) + " ($" + str(greatestIncrease) + ")")
    print("Greatest Decrease in Profits: " + str(greatestMonthD) + " ($" + str(greatestDecrease)+ ")")
    print("----------------------------------------------------------")

#output

    with open('financial_analysis.2.txt', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(monthCount) + "\n")
        text.write("    Total Profits: " + "$" + str(totalRevenue) +"\n")
        text.write("    Average Change: " + '$' + str(int(averageChanges)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(greatestMonthI) + " ($" + str(greatestIncrease) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(greatestMonthD) + " ($" + str(greatestDecrease) + ")\n")
        text.write("----------------------------------------------------------\n")




   
