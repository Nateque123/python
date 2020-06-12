# Example of Function inside function
# How to call other function

def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c): 
    return greater(greater(a,b), c) #First it will check from A or B which is greatest then if A is greatest then it will check A or C which is greatest.

num1 = int(input("Enter A : "))
num2 = int(input("Enter B : "))
num3 = int(input("Enter C : "))

print(f"{greatest(num1,num2,num3)} is Greatest")