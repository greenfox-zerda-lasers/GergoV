import csv

f = open('data.csv', newline='')
reader = csv.reader(f)
'''
if len(reader) == 0:
    print('Win')
'''

print(reader.line_num)

for row in reader:
    print(reader.line_num, '-', ''.join(row))
