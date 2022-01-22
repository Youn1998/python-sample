import urllib.request as req
import datetime
# URLや保存ファイル名を指定
def download(url):
  """天気予報APIアクセス

  Args:
      url (str): 天気予報APIエンドポイント

  Returns:
      str: ダウンロードしたJSONファイル名
  """
  date_suffix = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('_%Y_%m_%d')
  file_name = 'forecast'+date_suffix+'.json'
  # ダウンロード
  req.urlretrieve(url, file_name)
  return file_name