# Print how many times user char are in his name using For loop

uname = input("Enter your name: ") 
temp = ""

for i in range (0,len(uname)):
    if uname[i] not in temp:
        print(f"{uname[i]} : {uname.count(uname[i])}")
        temp += uname[i]