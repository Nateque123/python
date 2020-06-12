#Simple if elif and else condition example

age = int(input("Enter your age: "))
if age<=0:
    print("You can't watch it")
elif 1<age<=3:
    print("You can watch it free")
elif 3<age<=10:
    print("Give 100 rs please")
elif 10<age<=60:
    print("Give 150 rs please")
else:
    print("Give 200 rs please")