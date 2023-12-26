
#Create a program that checks if a number is even or odd.


def check_num(n):
    if n%2 == 0:
        return "The given Number is: Even "
    else:
        return "The given Number is: ODD "
        
n = int(input("Enter the Number: "))
Even_Odd = check_num(n)