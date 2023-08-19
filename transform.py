import json
import csv
import os
import re


# 各測定値が数字と単位を合わせて表記されているので、数字だけ取り出す関数を作る
def extract_numbers(input_string):
    numbers = re.findall(r'\d+\.\d+|\d+', input_string)
    return [float(num.replace(',', '.')) for num in numbers]


with open(os.path.join('output', "output_sample.json"), 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

output = []

for date in raw_data.keys():
    if raw_data[date] == {}:
        output.append([date, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    else:
        oneday_data = []
        for key in raw_data[date].keys():
            oneday_data.append(extract_numbers(raw_data[date][key])[0])
        output.append([date] + oneday_data)

# ファイルへの書き出し
with open(os.path.join('output', 'output.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['日付', '体重', '体脂肪率', '筋肉量', '筋肉スコア', '内臓脂肪レベル', '基礎代謝量', '体内年齢', '推定骨量', '体水分率'])
    for item in output:
        writer.writerow(item)
