#Write a program that prints the first 10 numbers in the Fibonacci sequence.

def check_febonacci(n):
    a,b = 0,1
    count = 0
    if n <= 0:
        print("Give the positive integer")
    if n == 1:
        print("Fibonacci sequence upto",n, ":")
        print(a)
    else:
        print("Fibonacci sequence: ")
        while count < n:
            print(a)
            nth = a + b
            a = b
            b = nth
            count += 1
check_febonacci(10)