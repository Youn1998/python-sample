from module.download import download
from module.read_weather import read_weather
import os
import common.constants as consts

def weather_forecast(area):
  """天気予報

  Args:
      area (str): 検索地域

  Returns:
      list[str]: 検索結果
  """
  # 気象庁から天気予報データをダウンロード
  file_name = download(consts.url)
  # 天気予報データを読み込み
  res = read_weather(file_name,area)
  # ダウンロードしたファイルを削除する
  os.remove(file_name)
  return res
