a = int(input('1つ目の整数を入力してください > '))
b = int(input('2つ目の整数を入力してください > '))
result = a-b
if result < 0:
  print('計算結果 : {}'.format(-result))
else:
  print('計算結果 : {}'.format(result))