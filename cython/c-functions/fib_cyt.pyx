cpdef int fib_cy(int n):
    if n < 2:
        return n
    return fib_cy(n-2) + fib_cy(n-1)
# cpdef because it also is called from python