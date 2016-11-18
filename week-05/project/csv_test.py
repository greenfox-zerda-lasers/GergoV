import csv

f = open('data.csv', newline='')
reader = csv.reader(f)
rownum = 0
for row in reader:
    rownum += 1
    print(rownum, '-', ''.join(row))
