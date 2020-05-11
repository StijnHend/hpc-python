import time
import fib
from fib_cyt import fib_cy

n = 30

# pure python recursive
s1 = time.perf_counter()
f1 = fib.fibonacci(n)
print(time.perf_counter() - s1)
print(f1)

# cython reduced overhead
s2 = time.perf_counter()
f2 = fib_cy(n)
print(time.perf_counter() - s2)
print(f2)

# pure python efficient using numpy
s3 = time.perf_counter()
f3 = fib.fib_fast(n)
print(time.perf_counter() - s3)
print(f3)