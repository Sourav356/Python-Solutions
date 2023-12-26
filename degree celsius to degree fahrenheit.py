def temp_Conversation(temp):
    if temp == "C":
        n =float(input("Enter Your temp in celsius: "))
        c_to_f =(n * 9/5) + 32
        print("Celsius to Fahrenheit of",n,"°C is = ",c_to_f,"°F")
    elif temp == "F":
        n =float(input("Enter Your temp in Fahrenheit: "))
        f_to_c =(n-32) * 5/9
        print("Fahrenheit to Celsius of",n,"°F is = ",f_to_c,"°C")
        
    else:
        print("Choose a correct sacle of temperature conversation.")
temp =input("Enter your sacle celsius as C for Celsius to Fahrenheit conversation and Fahrenheit as F for Fahrenheit to Celsius conversation : ")    
temp_Conversation(temp)