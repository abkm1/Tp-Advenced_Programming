while True:
    
    user_input = input("Please type in a string: ")
    if user_input == "":
        break
    
   
    print(user_input)
    print("\033[4m" + user_input + "\033[0m")