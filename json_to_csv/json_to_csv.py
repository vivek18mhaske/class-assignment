import json
import csv


with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(data[0].keys())
    for item in data:
        writer.writerow(item.values())

print("JSON data successfully converted to CSV")