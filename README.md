# healthplanet-datacollect
タニタのヘルスプラネットから過去のデータを取得する。APIではなく、requestsを使ったスクレイピングにて実施。

# 使い方
windowsでの使用を想定している。
初めに、app.py内の、initial_date、stop_dateを要件に合わせて修正しておく。

```
mkdir output
python app.py <ユーザ名> <パスワード>
python transform.py
```

これでoutput内にCSVが出力される。

# タニタの利用規約
https://www.healthplanet.jp/info/termsofuse.jsp
