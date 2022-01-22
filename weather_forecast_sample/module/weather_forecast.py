from module.download import download
from module.read_weather import read_weather
import os
import common.constants as consts

def weather_forecast(area):
  file_name = download(consts.url)
  res = read_weather(file_name,area)
  os.remove(file_name)
  return res
