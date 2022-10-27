import csv
import sys

final_list = []

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
try:
    file = open(sys.argv[1])
    file.close()

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for line in reader:
        lst, fst = line['name'].split(',')
        fst = fst.strip()
        final_list.append({'first': fst, 'last': lst, 'house': line['house']})

with open(sys.argv[2],'w') as file:
    writer = csv.DictWriter(file, ['first', 'last', 'house'])
    writer.writeheader()
    for item in range(len(final_list)):
        writer.writerow(final_list[item])



