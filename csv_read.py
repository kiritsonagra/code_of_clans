import csv

with open('data_file.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Column names are "+ ", ".join(row))
            line_count += 1
        else:
            print(row[0], row[1], row[2])
            line_count += 1
    print('Processed {} lines.'.format(line_count))
