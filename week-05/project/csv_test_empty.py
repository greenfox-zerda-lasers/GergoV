import csv

f = open('data2.csv', 'r', newline='')
reader = csv.reader(f, delimiter=',')

f.seek(0)
first_char = f.read(1)
if not first_char:
    print("E!")
else:
    for row in reader:
        rowcontent = ''.join(row)
        print(reader.line_num, '-', rowcontent)
