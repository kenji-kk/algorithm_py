#非負の整数の階乗値を求める
def factorial(n: int) -> int:
  if n > 0:
    return n * factorial(n - 1)
  else:
    return 1
