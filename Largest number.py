#prog to find largest number
#USN : 1RUA25BCA0029
#Name : Diganth 




a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))

if a>b and a>c:
    print("Largest number is",a)
elif b>a and b>c:
    print("Largest number is",b)
else:
    print("largest number is",c)
