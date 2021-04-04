#リストの全要素を走査（要素数を事前に取得）
x = ["aaa","bbb","ccc","ddd","1"]
for i in range(len(x)):
  print(f'x[{i}] = {x[i]}'')

#リストの全要素をenumerate関数で走査
x = ["aaa","bbb","ccc","ddd","1"]
for i, name in enumerate(x):
  print(f'x[{i}] = {name}')

#リストの全要素をenumerate関数で走査（１からカウント）
x = ["aaa","bbb","ccc","ddd","1"]
for i, name in enumerate(x, i):
  print(f'{i}番目 = {name}')

#リストの全要素を走査（インデックスを使わない）
x = ["aaa","bbb","ccc","ddd","1"]
for i in x:
  print(i)
