# -*- coding: utf-8 -*-
#n個の記号文字*をw個ごとに改行しながら表示
#for文の中にif文が混ざっており、ダメな例
print('記号文字*を表示します')
n = int(input('全部で何個：'))
w = int(input('何個ごとに改行：'))

for i in range(n):
  print("*", end = "")
  if i % w == w - 1:
    print()

if n % w:
  print()

#for文の中にif文を含めない良い例
print('記号文字*を表示します')
n = int(input('全部で何個：'))
w = int(input('何個ごとに改行：'))

for _ in range(n // w):
  print('*' * w)

  rest = n % w
  if rest:
    print('*' * rest)
