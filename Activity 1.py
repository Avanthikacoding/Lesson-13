print("Half Pyramid patterns of equals (=):")
a = int(input("Enter the mumber of rows: "))
for i in range(a):
    for j in range(i+1):
        print("= " , end="")
    print()