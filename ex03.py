total_amount = float(input("Total amount: "))
nb_Items = int(input("Number of items: "))
day_of_week = input("Day of the week: ")

if(total_amount>0 and nb_Items>0):
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',]
    weekend = ['saturday', 'sunday']
    if day_of_week.lower() in days_of_week :
             discounted_price = total_amount * (0.9)
    elif day_of_week.lower() in weekend: 
           discounted_price = total_amount * (0.8 )
    else:
           print("Invalid day of the week!")
           exit()
if nb_Items > 5:
    discounted_price *= 0.95
print(f"Total price after discount: {discounted_price:.1f} dinars")