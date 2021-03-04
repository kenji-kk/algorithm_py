#1から12までを8をスキップして繰り返す
#ダメなら例
for i in range(1,100):
  if i == 8:
    continue
  print(i, end='')
print()

#良い例
for i in list(range(1, 100)) + list(range(9, 13)):
  print(i, end=' ')
print()
