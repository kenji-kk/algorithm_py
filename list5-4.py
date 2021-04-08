def recur(n: int) -> int:
  """末尾再帰を「除去した関数recur"""
  while n > 0:
    recur(n - 1)
    print(n)
    n = n -2
