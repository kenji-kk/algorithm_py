#1から12までを8をスキップして繰り返す
#ダメなら例
for i in range(1,15):
  if i == 8:
    continue
  print(i, end='')
print()
