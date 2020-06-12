# Example of Fibonacci series

def Fibonacci_seq(n):
    a = 0
    b = 1
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")

num = int(input("Enter any number: "))
Fibonacci_seq(num)