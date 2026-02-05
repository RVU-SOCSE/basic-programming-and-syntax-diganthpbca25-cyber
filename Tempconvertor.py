
#prog to find temperature
#USN : 1RUA25BCA0029
#Name : Diganth P


print("i.celcius to fahrenheit conversion")
print("i.fahrenheit to celcius conversion")

choice = int(input("Enter your choice"))
temp = float(input("Enter the temperature"))
match choice:
    case 1:
        fahrenheit = (temp * 9/5)+32
        print("The fahrenheit temperature is",fahrenheit)
    case 2:
        celcius = (temp - 32)*5/9
        print("The celcius temperature is",celcius)
    case _:
        print("Invalid")
