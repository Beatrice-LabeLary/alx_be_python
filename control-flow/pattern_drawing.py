
size = int(input("Enter the size of the pattern:"))
count = 0
while count < size:
    for i in range (1,size + 1):
        print("*", end="")
    print("\n")
    count += 1