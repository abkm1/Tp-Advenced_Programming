
word = input("Word: ")


width = 30

for i in range(width):
    print("*", end="")
print()  


spaces_needed = width - len(word) - 2  
spaces_left = spaces_needed // 2
spaces_right = spaces_needed - spaces_left

print("*" + " " * spaces_left + word + " " * spaces_right + "*")


for i in range(width):
    print("*", end="")
print() 