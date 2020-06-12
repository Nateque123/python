# Take name and age from user and tell them that they can watch movies or not 

uname, age = input("Enter your name and age: ").replace(" ","").split(",")
uage = int(age)
if (uname[0] == "a" or uname[0:1] == "A") and uage >= 10:
    print(f"{uname}, You can watch movies")
else:
    print(f"sorry {uname}, you cannot watch movies")