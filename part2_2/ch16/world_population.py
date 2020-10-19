import json

filename = './data2/eq_data_1_day_m1.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dictp['Year'] == '2010'