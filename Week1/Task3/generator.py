def fibonacci(n):
    a = 0   
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b

def range_gen(n):
    for i in range(n):
        yield i

print("Printing fibonacci series of 10 numbers:")
for num in fibonacci(10):
    print(num, end=" ")

print("Printing range using generators till 10:")
for i in range_gen(10):
    print(i, end=" ")