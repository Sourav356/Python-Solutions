def mtableNo(n):
    if n > 0:
        print("The Multiplication table of the number", n, "is:")
        for i in range(1, 11):
            result = i * n
            print(f"{n} * {i} = {result}")
    else:
        print("Please enter a positive number")

n = int(input("Enter the number for which you want the Multiplication Table: "))
mtableNo(n)
