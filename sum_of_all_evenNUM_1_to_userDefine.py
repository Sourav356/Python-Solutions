def sum_of_even(n):
    sum_even = 0
    for i in range(1,n+1):
        if i%2==0:
            sum_even =sum_even+i
    print("The sum of the even number from 1 to",n,"is: ",sum_even)


n = int(input("Enter your limit: "))
sum_of_even(n)