#Write a program to check if a given string is a palindrome.

#i.Using Slicing

def isPalindrome(n):
    n = n.lower()
    if n == n[::-1]:
        return  ("The String is Palindrome")
    else:
        return  ("The given string is not Palindrome") 
    
n = input ("Enter Your string: ")
rev = isPalindrome(n)
print(rev)

#ii.Without slicing

def isPalindrome(n):
    n = n.lower()
    left,right = 0, len(n) - 1
    while left < right:
        if n[left] != n[right]:
            return ("The given string is not Palindrome")
        left += 1
        right -= 1
    return ("The String is Palindrome")
    
n = input ("Enter Your string: ")
rev = isPalindrome(n)
print(rev)