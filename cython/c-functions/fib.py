import numpy as np
from functools import lru_cache

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    f = np.empty(n+1, dtype=np.int32)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-2] + f[i-1]
    return f[-1]