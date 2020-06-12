# Guess the number and print guess times

import random
win_num = random.randint(1,99)
# Method 1 by For loop
# guess = 1
# for i in range(1,99):
#     unum = int(input("Enter your number: "))
#     if unum < win_num:
#         print(f" you entered {unum} which is low value, please increase it")
#     elif unum > win_num:
#         print(f" you entered {unum} which is high value, please decrease it")
#     else:
#         print(f"Congrats! You entered correct value {unum} in {guess} guess")
#         break
#     guess += 1


# Method 2 by While loop
unum = int(input("Enter Guess number: "))
game_over = False
guess = 1

while not game_over:
    if unum == win_num:
        print(f"Congrats! Your number {unum} is correct,\nYou guess it in {guess} times")
        game_over = True
    else:
        if unum < win_num:
            print(f"Your number {unum} is low, increase it")
        else:
            print(f"Your number {unum} is high, decrease it")
        unum = int(input("Enter again: "))  
    guess += 1