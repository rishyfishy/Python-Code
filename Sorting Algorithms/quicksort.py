def quicksort(array):
    '''
    repetitively partition the list using the first element as th
    '''
    if len(array) < 2:
        return array
    pivot = array[0]
    smaller,bigger = partition(array[1:], pivot)
    smaller = quicksort(smaller)
    bigger = quicksort(bigger)

    return smaller + [pivot]+ bigger

def partition(array:list,pivot:int):
    '''
    return all the elements that are smaller 
    and all the elements that are bigger than 
    the pivot as two separate lists.
    '''
    smaller=[]
    bigger=[]
    for item in array:
        print('t')
        if item<=pivot:
            smaller.append(item)
        else:
            bigger.append(item)
    return smaller, bigger

# print(quicksort([6,1,5,2,4]))