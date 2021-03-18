#リストの全要素を走査（要素数を事前に取得）
x = ["aaa","bbb","ccc"]
for i in range(len(x)):
  print(f'x[{i}] = {x[i]}'')

#リストの全要素をenumerate関数で走査
x = ["aaa","bbb","ccc"]
for i, name in enumerate(x):
  print(f'x[{i}] = {name}')
