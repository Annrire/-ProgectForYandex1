import csv

list1 = 'Anna'
list2 = '250'
sps = []
data = []
data.append([list1, list2])
path = "records1.csv"
with open(path, "a") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
        writer.writerow(line)
with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        if len(row) != 0:
            sps.append(row)
print(sps)