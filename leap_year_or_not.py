def lepYear(n):

    if n%4==0 and n%100 != 0 or n%400 == 0 :
        print("The Year",n,"is a Leap year")
    else:
        print( "The year",n,"is not a Leap year")
        print("The year you are given that is lies between the below years and those years are not a Leap Year.", "\n The list -  1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600, 2700, 2900, 3000")
   
n = int(input("Enter the year: "))
lepYear(n) 