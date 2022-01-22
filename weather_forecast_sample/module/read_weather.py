import json

def read_weather(file_name,search_area):
  """予報情報読み込み

  Args:
      file_name (str): ダウンロードしたJSONファイル名
      search_area (str): 検索地域

  Returns:
      list[str]: 検索結果
  """
  with open(file_name,'r',encoding='UTF-8')as f:
    data = json.load(f)

  return_labels = []
  for area in data:
    name=area['name']
    if search_area == name:
      return_labels.append(name)
      for ts in area['srf']['timeSeries']:
        times = [n for n in ts['timeDefines']]
        if 'weathers' in ts['areas']:
          for i,v in enumerate(ts['areas']['weathers']):
            return_labels.append(times[i]+":"+v)
  return return_labels