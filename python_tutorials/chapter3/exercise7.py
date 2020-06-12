# Take name of user and print how many times characters are present in name

name = input("Enter your name: ")

i = 0
total = ""
while i < len(name):
    if name[i] not in total:
        total += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1