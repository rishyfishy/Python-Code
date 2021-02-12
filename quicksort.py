def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    smaller,bigger = partition(array[1:], pivot)
    smaller = quicksort(smaller)
    bigger = quicksort(bigger)

    return smaller + [pivot]+ bigger

def partition(array:list,pivot:int):
    smaller=[]
    bigger=[]
    for item in array:
        if item<=pivot:
            smaller.append(item)
        else:
            bigger.append(item)
    return smaller, bigger

print(quicksort([5,2,1,6,4]))