numbers = [1, 2, 3, 4, 5]
print(numbers)

while True :
    input_index=input(print("enter an index"))
    input_value=input(print("enter an value"))
    if input_index == -1:
        break
    else :
     if 0 <= input_index < len(numbers):
       numbers[input_index]=input_value
       print(f"updated list : {numbers}")
     else:
        print("Invalid index. Try again.")
