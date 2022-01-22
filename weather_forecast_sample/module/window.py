from tkinter import *
from tkinter import ttk
from module.weather_forecast import weather_forecast
import common.constants as consts

def window():
  def search(event):
    results = weather_forecast(search_area.get())
    text.set("\n".join(results))

  # Tkクラス生成
  root = Tk()
  # # 画面サイズ
  # root.geometry('600x400')
  # 画面タイトル
  root.title('天気予報')

  frame = ttk.Frame(root,padding=10)
  frame.grid()

  label = Label(frame, text="天気予報",anchor='center')

  search_area = StringVar()

  condition = ttk.Combobox(
    frame,
    textvariable=search_area,
    values=consts.areas,
    width=15
  )
  condition.set('東京')

  button = Button(
    frame,
    text='検索',
    width=10,
    anchor="center"
  )

  text = StringVar()
  text.set("ここに結果が表示されます。")
  result = Label(
    frame,
    textvariable=text,
    anchor='center',
    justify='left'
  )

  label.pack()
  condition.pack()
  button.bind('<Button>',search)
  button.pack()
  result.pack()
  # 画面をそのまま表示
  frame.mainloop()