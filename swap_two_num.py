#How can you swap the values of two variables with using a temporary variable?


#1.With 3rd variable 

A = int(input("Give the first  value: "))
B = int(input("Give the second Value: "))
print(A,B)
temp = A
A = B
B = temp
print("After swap: ", A,B)
 
#Do same thing using  Function

def swapTwo(A,B):
    print("Before swap using def values are: ",A,B)
    temp = A
    A = B
    B = temp
    return A,B
    
A = int(input("Enter your number A:  "))
B = int(input("Enter your number B:  "))
print("After Swap using def values are:", swapTwo(A,B))