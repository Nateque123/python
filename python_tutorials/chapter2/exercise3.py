#Take name and one char from user and print length of name and how many times that char comes in it.

# name, w_name = input("Enter your name: ").split(",")
# print(f"Length of your name is {len(name)}")
# print(f"{w_name.strip()} is present {name.strip().lower().count(w_name.strip().lower())} times in {name}")

#Method Two
name, char = input("Enter your name and one char: ").replace(" ","").split(",")
print(f"Length of your name {name} is \"{len(name)}\"")
print(f"character {char} comes \"{name.count(char)}\" times in {name}")