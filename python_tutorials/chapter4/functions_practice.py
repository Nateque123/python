# Functions Practice

# def last_char(n):
#     return n[-1]

# name = input("Enter your name: ")
# print(f"Your names last character is \"{last_char(name)}\"")

# def odd_even(n):
#     if n%2 == 0:
#         return "Even"
#     return "Odd"

# num = int(input("Enter number: "))
# print(f"Your number {num} is {odd_even(num)}")

def is_even(n):
    return n%2 == 0 #Shortest way, It will return True or False Value

num = int(input("Enter any number: "))
print(f"Your number {num} is {is_even(num)}")

