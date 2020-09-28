import csv
import json
from collections import OrderedDict

csvfile = open('영양소정보.csv', 'r')
funcfile = open('효능.csv', 'r')
jsonfile = open('../nutrients.json', 'w', encoding='UTF-8')

field_names = (
    "precaution",
    "limit_high",
    "name",
    "limit_low",
    "functionals"
)

func_field_names = (
    "category",
    "content"
)

func_data = []
func_reader = csv.DictReader(funcfile, func_field_names)
for i, row in enumerate(func_reader):
    if i == 0:
        continue
    new_row = OrderedDict()
    new_row['model'] = 'supplements.functional'
    new_row['pk'] = i
    new_row['fields'] = row
    func_data.append(new_row)
# print(func_data)

reader = csv.DictReader(csvfile, field_names)
data = []
for i, row in enumerate(reader):
    if i == 0:
        continue
    func = row['functionals']
    func_arr = func.split(',')
    # print(func_arr)
    func_ids = []
    for words in func_arr:
        words = words.strip()
        for d in func_data:
            if d['fields']['content'] == words:
                func_ids.append(d['pk'])
    if not len(func_ids):
        func_ids = []
    row['functionals'] = func_ids
    row['limit_high'] = 10000000 if not row['limit_high'] else float(
        row['limit_high'])
    row['limit_low'] = 0 if not row['limit_low'] else float(
        row['limit_low'])
    new_row = OrderedDict()
    new_row['model'] = 'supplements.nutrient'
    new_row['pk'] = i
    new_row['fields'] = row
    data.append(new_row)
    # print(i)
jsonfile.write(json.dumps(data, ensure_ascii=False))
