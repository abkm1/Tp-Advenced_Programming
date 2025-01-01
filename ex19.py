unique_words = set()
list_dup = []

while True:
    input_word = input("Enter a word: ").strip()
    if input_word == "":
        print(f"You entered {len(unique_words)} unique words and {len(list_dup)} duplicate words.")
        break
    if input_word.lower() in unique_words:
        list_dup.append(input_word)
    else:
        unique_words.add(input_word.lower())  # The lower makes the program case insensitive
        print(sorted(unique_words))

while True:
    user_choice = input("Do you want to save it to a file? 1. Yes 2. No: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            with open("unique_words.txt", "w") as file:
                for word in sorted(unique_words):  # Sort for file saving
                    file.write(word + "\n")
            print("File saved successfully.")
            break
        elif user_choice == 2:
            print("Operation canceled.")
            break
        else:
            print("Invalid input, enter 1 or 2.")
    else:
        print("Invalid input. enter a number.")
