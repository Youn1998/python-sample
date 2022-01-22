# Weather Forecast Sample

## Overview
気象庁 天気予報APIを使用した天気予報取得Pythonアプリ

## Requirement
- Python 3.x.x

## DirectoryStructure
- common：共通部品置き場
- module：各処理置き場
  - download.py：天気予報データを取得する
  - read_weather.py：天気予報データを検索する
  - window.py：天気予報ダイアログを表示する
- app.py：アプリのエントリーポイント

## Tips
### 実行前にやること
``` zsh
python3
>>> certifi.where()
# /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/certifi/cacert.pem

export SSL_CERT_FILE=/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/certifi/cacert.pem
```

### 実行
```zsh
python3 app.py
```