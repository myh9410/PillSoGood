import csv
import json
from collections import OrderedDict

csvfile = open('영양제정보(칼럼수정).csv', 'r')
nutfile = open('영양소정보.csv', 'r')
jsonfile = open('../supplements.json', 'w', encoding='UTF-8')

field_names = (
    "dosage",
    "name",
    "nutrients",
    "expiration_date",
    "storage_method",
    "manufacturer",
    "product_form"
)

nut_field_names = (
    "precaution",
    "limit_high",
    "name",
    "limit_low",
    "functionals"
)

nut_reader = csv.DictReader(nutfile, nut_field_names)
nut_data = []
for i, row in enumerate(nut_reader):
    if i == 0:
        continue
    new_row = OrderedDict()
    new_row['model'] = 'supplements.nutrient'
    new_row['pk'] = i
    new_row['fields'] = row
    nut_data.append(new_row)

reader = csv.DictReader(csvfile, field_names)
data = []
for i, row in enumerate(reader):
    if i == 0:
        continue
    # print(row['nutrients'])
    nut = row['nutrients']
    nut_arr = nut.split(',')
    # print(func_arr)
    nut_ids = []
    for words in nut_arr:
        words = words.strip()
        for d in nut_data:
            if d['fields']['name'] == words:
                nut_ids.append(d['pk'])
    row['nutrients'] = nut_ids
    new_row = OrderedDict()
    new_row['model'] = 'supplements.supplement'
    new_row['pk'] = i
    new_row['fields'] = row
    data.append(new_row)
jsonfile.write(json.dumps(data, ensure_ascii=False))
