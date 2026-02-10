# Factorial of a number using Recursion
#USN: 1RUA25BCA0029
#Name: Diganth P


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
