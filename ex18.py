
numbers = [1, 2, 3, 4, 5]

print("Menu:")
print("1. Append")
print("2. Insert")
print("3. Pop")
print("4. Remove")
print("5. Quit")

while True:
    try:
        user_choice = int(input("Choose an option: "))

        if user_choice == 1:
            value = int(input("Enter value: "))
            numbers.append(value)
            print(f"Updated List: {numbers}")

        elif user_choice == 2:
            index = int(input("Enter an index: "))
            value = int(input("Enter a value: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print(f"Updated List: {numbers}")
            else:
                print("Invalid index")

        elif user_choice == 3:
            if numbers:
                numbers.pop()
                print(f"Updated List: {numbers}")
            else:
                print("The list is already empty")

        elif user_choice == 4:
            value = int(input("Enter a value: "))
            if value in numbers:
                numbers.remove(value)
                print(f"Updated List: {numbers}")
            else:
                print("This value doesn't exist in the numbers list")

        elif user_choice == 5:
            print("Quit")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid input. Please enter a number.")
