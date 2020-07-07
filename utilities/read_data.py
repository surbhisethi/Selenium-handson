import csv

def getCSVData(fileName):

    #create an empty list to store data
    rows= []

    #open the CSV File
    dataFile = open(fileName, "r")

    #create a CSV Reader from CVS File
    reader = csv.reader(dataFile)

    #skip the headers
    next(reader)

    #add rows from reader to lists
    for row in reader:
        rows.append(row)
    return rows