# Take input 3 inputs as a int and print average using String formatting

no1, no2, no3 = input("Enter three numbers: ").split(",")
average = (int(no1)+int(no2)+int(no3))/3
print(f"Your Average of {no1}, {no2} and {no3} is {average}")