# Sum of each number given by user

num = input("Enter more than one digit number: ")
total = 0
for i in range (0,len(num)):
    total += int(num[i])
    i += 1

print(f"Total of your {num} is {total}")