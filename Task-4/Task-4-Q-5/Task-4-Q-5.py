rows=int(input("Enter The Number Of Rows:"))
for i in range(rows):
    for space in range(rows-i-1):
        print(end=" ")
    for star in range(i+1):
        print("*",end=" ")
    print()