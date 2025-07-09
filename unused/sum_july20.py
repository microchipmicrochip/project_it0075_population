import csv

total = 0
with open('province-data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader, 1):
        if 133 <= i <= 161 and row[0] == 'Cagayan':
            try:
                total += int(row[2])
            except (IndexError, ValueError):
                pass
print('Sum of July 20 for Cagayan province, lines 133-161:', total)
