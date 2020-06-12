# Function for telling which number is greater

def greater_fun(a,b):
    if a>b:
        return a
    return b

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"{greater_fun(num1,num2)} is greater")