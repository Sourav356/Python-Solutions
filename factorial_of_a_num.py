#Calculate the factorial of a number using a loop 

n = int(input("Give the number for which want factorial: "))
count = 0
A_fact = 1
while count < n:
    fac =n - count
    A_fact *= fac
    count +=1
print(A_fact)
    
 #Using Function   
 
def factorial(n):
    count = 0
    A_fact = 1
    while count < n:
        fac = n - count
        A_fact *= fac
        count += 1
    return A_fact
        
n = int(input("Give the number for which you want factorial: ")) 
factorial = factorial(n)
print("Factorial of", n , "is = ", factorial)