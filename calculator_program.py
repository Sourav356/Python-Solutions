sign =input("Enter your operation sign: ")

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
match sign :   #the "match" command only work on python version 3.10 or higher version for other down graded version you use "Switch" command.
    case '+':
        c= a+b
        print("After Addition: ",c)
    case '-':
        c = a-b
        print("After Subtraction: ",c)
    case '*':
        c = a*b
        print("After Multiplication: ",c)
    case '/':
        try:
            c = a/b
            print("After Division: ",c)
        except ZeroDivisionError as e:
            print(e, "is not possible as per the mathematical laws")
    case '%':
        try:
            c =(a/b)*100
            print("Percentage of the given numbers is: ",c)
        except ZeroDivisionError as e:
            print(e, "is not possible as per the mathematical laws")
    case _:
        print("Please enter a valid operation.",sign,"this operation is not listed.")