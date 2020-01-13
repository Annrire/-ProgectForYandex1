import csv

list1 = 'Anna'
list2 = '250'

data = []
data.append([list1, list2])
path = "records1.csv"
with open(path, "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
        writer.writerow(line)
with open(path, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
print(reader)