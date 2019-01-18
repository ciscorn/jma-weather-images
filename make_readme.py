import json


with open("codes.json", encoding="utf-8") as f:
    data = json.load(f)

print('|code|description|fkd|jtj|')
print('|:-:|---|:-:|:-:|')

for key in sorted(data.keys()):
    d = data[key]
    b = d["b"]
    m = d.get("m", "")
    t = d.get("t", "")
    print(f'| {key} | {b} {m} {t} | <img width="50" src="./output_refs/{key}.png" /> | <img width="50" src="./output/{key}.png" /> |')
