# Guess number by taking one number from user.

# import random
# for x in range(1):
#     winning_num = random.randint(1,99)
winning_num = 18
user_num = int(input("Enter guess Number: "))

if user_num==winning_num:
    print("You winn!!")
else: # Nested If Else
    if user_num<winning_num:
        print("Too low")
    else:
        print("Too High")