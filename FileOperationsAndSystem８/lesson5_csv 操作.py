import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    Writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    Writer.writeheader()
    Writer.writerow({'Name': 'A', 'Count': 1})
    Writer.writerow({'Name': 'B', 'Count': 2})
    Writer.writerow({'Name': 'C', 'Count': 3})
    Writer.writerow({'Name': 'D', 'Count': 4})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])





