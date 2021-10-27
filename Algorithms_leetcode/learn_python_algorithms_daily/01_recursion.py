#递归
def Fibonacci_recursion(n):
    if n<=2:
        return n
    return Fibonacci_recursion(n-1) + Fibonacci_recursion(n-2)

print(Fibonacci_recursion(10))

#循环
def Fibonacci(n):
    a,b = 0,1
    for i in range(n+1):
        a,b = b,a+b
    return a

print(Fibonacci(10))