name = "Nateq Siddiqui"

# Old traditional way
# for i in range(len(name)):
#     print(name[i])

# Python way
# for i in name:
#     print(i)

num = input("Enter more than one digit number: ")
total = 0
for i in num:
    total += int(i)
print(f"Your sum of {num} is {total}")