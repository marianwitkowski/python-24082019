
print("")
for i in range(0,11):
    if i==0:
        print(" "*3, end=' ')
    else:
        print(f"{i:3d}", end=' ')
print("")


print("-"*43)
for i in range(1,11):
    print(f"{i:2d}|",end=' ')
    for j in range(1,11):
        print(f"{i*j:3d}",end=' ')
    print("")
