from operator import itemgetter


cities = []


while True:
    list = []  
    city = input("Please type in the name of the city: ")
    
    if city == "stop":
        break  
    else:
       
        population = len(city) * 1000000
        list.append(city)
        list.append(population)
        cities.append(list)


sortedList = sorted(cities, key=itemgetter(1), reverse=True)

print("\nCity Populations (from largest to smallest):")
for city, population in sortedList:
    print(f"{city}: {population} citizens")
