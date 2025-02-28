import csv

csvfile = open("myfile3.csv", "r", newline='')
csvreader = csv.reader(csvfile)

header = next(csvreader, None)
print("Header:", header)
row = next(csvreader, None)
print("Row 1:")
print(row[0])  # Access the first column
print(row[1])  # Access the second column
row = next(csvreader, None)
print("Row 2:")
print(row[0])  # Access the first column
print(row[1])  # Access the second column
csvfile.close()
