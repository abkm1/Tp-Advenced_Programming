
nbr = int(input("nbr: "))
if nbr % 3 == 0 and nbr % 5 == 0:
    print("FizzBuzz")
elif nbr % 3 == 0:
    print("Fizz")
elif nbr % 5 == 0:
    print("Buzz")
