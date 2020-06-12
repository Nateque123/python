# Simple while loop examples

# i = 1
# while i<=10:
#     print(f"Value of i is {i}")
#     i += 1
    
unume = int(input("Enter number till where you want to do sum of numbers : "))
total = 0
i = 1
while i<=unume:
    total += i
    i += 1
    print(total)
        
print(f"Total number is {total}")