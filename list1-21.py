#多重プログラミング 九九の表示
print('---', * 10)
for i in range(1,15):
  for j in range(1, 15):
    print(f'{i * j:3}', end='')
  print()
print('--¥', * 10)
