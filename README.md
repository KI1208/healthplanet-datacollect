# healthplanet-datacollect
タニタのヘルスプラネットから過去のデータを取得する。APIではなく、requestsを使ったスクレイピングにて実施。
これはAPIだと、直近3か月分しか取得できない、体重と体脂肪率しか取得できないという制約があるため。

# 使い方
windowsでの使用を想定している。
初めに、app.py内の、initial_date、stop_dateを要件に合わせて修正しておく。

```
mkdir output
python app.py <ユーザ名> <パスワード>
python transform.py
```

これでoutput内にCSVが出力される。

## 可視化
CSVなのでエクセルなどで簡単に可視化はできるが、単体でもある程度見られるようにHTMLの可視化ツールを用意した。HTMLファイルをダブルクリックしてChromeなどで開き、CSVを指定すればよい。

# タニタの利用規約
https://www.healthplanet.jp/info/termsofuse.jsp
