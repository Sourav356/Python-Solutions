#Implement a program to find the maximum and minimum values in an array.
list = [4,6,5,2,3]
n_max =max(list)
n_min = min(list)
print("n_max =",n_max,"and n_min =",n_min)

#Using Function

def max_min(list):
    n_max =max(list)
    n_min = min(list)
    print("n_max =",n_max,"and n_min =",n_min)
    
list = []
for i in range(10):
    list.append(i)
print("your list is: ",list)
    
max_min(list)