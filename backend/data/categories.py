import csv
import json
from collections import OrderedDict

csvfile = open('효능 카테고리.csv', 'r')
jsonfile = open('../categories.json', 'w', encoding='UTF-8')

field_names = (
    "name",
)

reader = csv.DictReader(csvfile, field_names)
data = []
for i, row in enumerate(reader):
    if i == 0:
        continue
    new_row = OrderedDict()
    new_row['model'] = 'supplements.category'
    new_row['pk'] = i
    new_row['fields'] = row
    data.append(new_row)
print(data)
jsonfile.write(json.dumps(data, ensure_ascii=False))
