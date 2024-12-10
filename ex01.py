name = input("Please enter your name: ")
if name == "VIP":
    print("Enjoy the show for free!")
else:
    tickets = int(input("How many tickets would you like to buy? "))
    totCost = tickets * 15.50
    print(f"The total cost is {totCost}")
    print("Enjoy your tickets!")