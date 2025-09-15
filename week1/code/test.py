from time import time  

def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

t0 = time()
n = 48
ans = fib(n)
t1 = time()
print(f"Computed fib {n} = {ans} in {t1- t0} s")