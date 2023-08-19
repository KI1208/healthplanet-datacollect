import sys
import os
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import json
import csv


import requests
from bs4 import BeautifulSoup


username = "KI1208"
password = "t@2tak12k"
login_url = "https://www.healthplanet.jp/login.do"

health_data = []

# セッションのインスタンスを作成する。
session = requests.Session()

# ログインの実施。見た目はユーザ名とパスワード(と次回以降の自動ログイン有無)のみだが、hidden inputがあるので、それも埋める。
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

soup = BeautifulSoup(response_1.content, 'html.parser')

# テーブルから測定情報を取得し、jsonに
output_json = {}
table = soup.find_all("table", class_="inputDataTable")
rows = table[1].findAll("tr")

# 取得したデータが、<th>体重<td>65.70kg</td></th>となってしまっているので、thの方はsplitして本来の見出しの方だけ取り出す。
for row in rows:
    output_json[row.find("th").text.split()[0]] = row.find("td").text.strip()

print(output_json)

with open(os.path.join("output", "output.json"), 'w', encoding='utf-8') as f:
    json.dump(output_json, f, ensure_ascii=False, indent=4)

# response_2 = session.get(
#         url="https://www.healthplanet.jp/innerscan.do?date=20230701"
#     )
# print(response_2.text)
