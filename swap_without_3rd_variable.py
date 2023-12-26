#How can you swap the values of two variables without using a temporary variable?

def swapTwo(A,B):
    print("Before swap using without 3rd vari in def values are: ",A,B)
    A = B + A
    B = A - B
    A = A - B
    return A,B
A = int(input("Enter your number A:  "))
B = int(input("Enter your number B:  "))
A,B = swapTwo(A,B)
print("After Swap using without 3rd vari in def values are:", A,B)