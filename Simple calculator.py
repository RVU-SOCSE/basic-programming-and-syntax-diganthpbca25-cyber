
#prog to find simple calculator
#USN : 1RUA25BCA0029
#Name : Diganth P




a = int(input("Enter the a value"))
b = int(input("Enter the b value"))

operator = input("Enter the operator")

match operator:
    case '+':
       print("result is ", a + b)
    case '-':
       print("result is ", a - b)
    case '*':
       print("result is ", a * b)   
    case '/':
       print("result is ", a / b)
    case '%':
       print("result is ", a % b)  
    case _:
       print("Error")
          
