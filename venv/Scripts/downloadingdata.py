import csv

filename = 'C:/Users/olwyn/PycharmProjects/pythonProject1/venv/Scripts/data/death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

