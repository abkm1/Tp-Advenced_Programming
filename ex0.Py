
nbPeople = int(input("How many people need a ride? "))
if nbPeople>0:
    capacity = int(input("How many people fit in one taxi? "))
    if capacity>0 :
      nbTaxisNeed = nbPeople//capacity
      remainder = nbPeople % capacity
      taxis_needed = nbTaxisNeed + (1 if remainder > 0 else 0)
      print(f"Number of taxis needed: {taxis_needed}")

else:
    print("Enter a positive number of people.")
