# Fibonnaci using recursion

def fib_rec(n):
  if n < 1:
    return 0
  if n == 1:
    return 1
  return fib_rec(n-1) + fib_rec(n - 2)

# Fibonnaci using recursion + memoization


def fib_memo(n, memo = {}):
  if n < 1:
    return 0
  if n == 1:
    return 1
  if n not in memo:
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
  return memo[n]
