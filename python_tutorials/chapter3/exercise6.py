# Ask user to input more than one digit number and calculate sum of each digit

num = input("Enter more than one digit num: ")

total = 0
i = 0
while i < len(num):
    total += int(num[i])
    i += 1

print(f"Sum of your number is {total}")