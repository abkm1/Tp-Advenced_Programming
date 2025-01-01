def Is_integer(s): #to check if the input is int before transformation the string to int 
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True
    
integer = input("enter a number: ")
if Is_integer(integer)  :
        integer = int(integer)
        if integer > 0 : 
            i = -(integer) 
            while (i<=integer) : 
                print(i)
                i+=1
        else : 
            print("This is not a positive numer")

else : 
     print("This is not a number")