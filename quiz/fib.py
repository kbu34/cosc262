def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        if n % 2 == 1:
            c = (n + 1) / 2
            f = fib(c)
            d = fib(c - 1)
            return f * f + d * d
        else:
            c = n / 2
            f = fib(c)
            return (2 * fib(c - 1) + f) * f
    
    
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(9))
print(fib(100))