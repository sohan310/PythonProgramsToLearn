n=5
print("1\n")
for i in range(n):
    for j in range(i+1):
        if(i==0 or j==i or i==n-1 or j==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("\n")
print("2\n")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        if(i==0 or i==k or k==0 or i==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("\n")
print("3\n")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    print()
print("\n")
print("4\n")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    print()
print("\n")

print("5\n")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
print("\n")
print("6\n")
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()
print("\n")
print("7\n")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
print("\n")

print("8\n")
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
print("\n")
print("9\n")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    print()
print("\n")
print("10\n")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
print("\n")
print("11\n")
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()
print("\n")
print("12\n")
for i in range(n):
    for j in range(n-i-1):
          print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i-1):
        print("*",end="")
    print()
print("\n")
print("13\n")
for i in range(n-1):
    for j in range(n-i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
print("\n")
print("14\n")
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i):
          print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
print("\n")
print("15\n")
for i in range(n-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()
print("\n")
print("16\n")
for i in range(n-1):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
