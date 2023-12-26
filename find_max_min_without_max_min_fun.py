#Implement a program to find the maximum and minimum values in an array without using max(), min() function.

def find_max_min(lst):
    if not lst:
        return None, None
    maximum =minimum = lst[0]
        
    for num in lst:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum , minimum
        
my_list = [7,8,3,5,9,1] 
max_val,min_val= find_max_min(my_list)

if max_val is not None and min_val is not None:
    print(f"maxvalue: {max_val}")
    print(f"minvalue: {min_val}")
else:
    print("This list is empty")