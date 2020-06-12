# Which number is greater from three

def greater_fun(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c

num1 = int(input("Enter A : "))
num2 = int(input("Enter B : "))
num3 = int(input("Enter C : "))

print(f"{greater_fun(num1,num2,num3)} is greater")