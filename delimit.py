#import pandas as pd

# df = pd.DataFrame(columns=['Token', 'POS', 'Chunk', 'NER'])
#
# f = open("conll2003/engsample.testa", "r")
# Lines = f.readlines()
#
# for line in Lines:
#     print(line)
#     res = line.split()
#     print(res)
#     df = df.append(res)
#
#
# df.to_csv("engtesta.csv")
import csv
with open('conll2003/eng.testb') as report:
    reader = csv.reader(report, delimiter=" ")
    with open('conll2003/engtestb.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in reader:
            writer.writerow(line)