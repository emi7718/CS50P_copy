import csv
import tabulate
import sys

lst = []

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif not sys.argv[1].endswith('.csv'):
    sys.exit('Not a csv file')
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit('File does not exist')

with open(sys.argv[1]) as csv_file:
    reader = csv.reader(csv_file)
    for lines in reader:
        lst.append(lines)
    headers = lst[0]
    table = lst[1:]
    print(tabulate.tabulate(table, headers, tablefmt='grid'))
