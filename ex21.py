def length(list): 
    i = 0
    while True:
        try:
            list[i]
            i += 1
        except IndexError:
            return i
def mean(list) : 
    sum = 0
    if length(list)!=0:
     for i in range(length(list)):
        sum += list[i]
     return sum / length(list)
    else:
        return sum 

def range_of_list(list) : 
    return max(list)-min(list)


print(length([1,2,3,4,5]))
print(mean([1,2,3,4,5]))
print(range_of_list([1,2,3,4,5]))