numbers=[]
shoe_sizes=[]
n=8
for i in range(5):
    numbers.append(i+1)
    shoe_sizes.append(n+i)

print(f"numbers : {numbers}")
print(f"shoe_sizes : {shoe_sizes}")
numbers.extend([3, 5 ,4 ,2])
print(f"Numbers with duplicates: {numbers}")
numbers = sorted(set(numbers))
print(f"Numbers without duplicates: {numbers}")
list = numbers + shoe_sizes
print(f"Combined List: {list}")