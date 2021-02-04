def findPythagoreanTripples(lst:list)->bool:
    if len(lst)<3: return False
    
    newDict={lst[i]**2:i for i in range(len(lst))}

    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if (lst[i]**2+lst[j]**2 in newDict):
                return True 
    return False