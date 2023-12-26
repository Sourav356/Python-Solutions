S_word = input("Enter the word: ")
count = 0

with open('text.txt', 'r') as file:  #You have to create the text.txt file 1st then do the code for error free exicusion.
    data = file.readlines()
    
    for line in data:
        if S_word in line:
            count += 1

print(count)
