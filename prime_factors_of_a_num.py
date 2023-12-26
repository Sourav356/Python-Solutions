def primeFact(n):
    if n > 1:
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)

        print("Prime factors of", n, "are:", factors)
    else:
        print("Please enter a positive number greater than 1.")

n = int(input("Enter the number for which you want the Prime factors: "))
primeFact(n)
