import csv
with open('eng.train') as report:
    reader = csv.reader(report, delimiter=' ')
    with open('engtrain.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in reader:
            writer.writerow(line)