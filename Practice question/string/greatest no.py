a = int(input("enter no 1 :"))
b = int(input("enter no 2 :"))
c = int(input("enter no 3 :"))

if (a >= b) and (a >= c):
    print(a, "is the highest no")
elif (b >=a) and (b >= c):
    print(b, "is the highest no")
else:
    print(c, "is the highest no")