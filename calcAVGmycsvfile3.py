import csv

csvfile = open("myfile3.csv", "r", newline='')
print("File Created")

csvreader = csv.reader(csvfile)
csvreader.writenow(['Name', 'Age', 'City'])
print("Colunms Created")

csvwriter.writerow(['Alice', 12, 'New York'])
print("Data Created")

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
