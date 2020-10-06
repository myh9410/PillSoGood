import csv
import json
from collections import OrderedDict

csvfile = open('효능.csv', 'r')
jsonfile = open('../functionals.json', 'w', encoding='UTF-8')
cat_csvfile = open('효능 카테고리.csv', 'r')

cat_field_names = (
    "name",
)

cat_reader = csv.DictReader(cat_csvfile, cat_field_names)
cat_data = []
for i, row in enumerate(cat_reader):
    if i == 0:
        continue
    new_row = OrderedDict()
    new_row['model'] = 'supplements.category'
    new_row['pk'] = i
    new_row['fields'] = row
    cat_data.append(new_row)
# print(cat_data)
field_names = (
    "category",
    "content"
)

reader = csv.DictReader(csvfile, field_names)
data = []
for i, row in enumerate(reader):
    if i == 0:
        continue
    # print(row['category'])
    for category in cat_data:
        # print(category['fields']['name'])
        if row['category'] == category['fields']['name']:
            row['category'] = category['pk']
        new_row = OrderedDict()
    new_row['model'] = 'supplements.functional'
    new_row['pk'] = i
    new_row['fields'] = row
    data.append(new_row)
# print(data)
jsonfile.write(json.dumps(data, ensure_ascii=False))
