## Example of CSV parsing with module CSV. work on file names.csv

import csv

# copy csv to new csv file with new delimiter -
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    # next(csv_reader)
    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)


