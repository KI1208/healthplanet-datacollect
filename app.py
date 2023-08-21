import sys
import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# ユーザ名とパスワードは都度指定する形に
username = sys.argv[1]
password = sys.argv[2]
login_url = "https://www.healthplanet.jp/login.do"


# URLに対象日時をいれるため、ジェネレータを定義する
def date_generator(initial_date, stop_date):
    current_date = initial_date
    while current_date - stop_date > timedelta(days=-1):
        yield current_date.strftime("%Y%m%d")
        current_date -= timedelta(days=1)


# セッションのインスタンスを作成する。
session = requests.Session()

# ログインの実施。見た目はユーザ名とパスワード(と次回以降の自動ログイン有無)のみだが、hidden inputがあるので、それも埋める。
# その中に日付指定する部分があるが、そこは適当に指定している
response_1 = session.post(
        url=login_url,
        data={
            "loginId": username,
            "passwd": password,
            "auto": "on",
            "send": 1,
            "url": "https://www.healthplanet.jp/innerscan.do?date=20230801"
        }
    )

# 日付回数分アクセスを実施、自分の場合は2021/8/11
initial_date = datetime(2023, 8, 18)
stop_date = datetime(2021, 8, 11)

date_gen = date_generator(initial_date, stop_date)
output_json = {}

for generated_date in date_gen:
    output_json[generated_date] = {}
    response_2 = session.get(
        url="https://www.healthplanet.jp/innerscan.do?date=" + generated_date
    )

    soup = BeautifulSoup(response_2.content, 'html.parser')

    # テーブルから測定情報を取得し、jsonに
    table = soup.find_all("table", class_="inputDataTable")
    if len(table) > 1:
        rows = table[1].findAll("tr")
    # 取得したデータが、<th>体重<td>65.70kg</td></th>となってしまっているので、thの方はsplitして本来の見出しの方だけ取り出す。
        for row in rows:
            output_json[generated_date][row.find("th").text.split()[0]] = row.find("td").text.strip()

# ファイルに書き出して終了
output_filename = 'output.json'
with open(os.path.join("output", output_filename), 'w', encoding='utf-8') as f:
    json.dump(output_json, f, ensure_ascii=False, indent=4)


