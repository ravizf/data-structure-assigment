call_naive = 0
call_memo = 0

def fib_naive(n):
    global call_naive
    call_naive += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

memo = {}
def fib_memo(n):
    global call_memo
    call_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

n = 10
print("Naive Fib:", fib_naive(n), "Calls:", call_naive)
print("Memo Fib:", fib_memo(n), "Calls:", call_memo)
