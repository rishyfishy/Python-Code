import datetime

Input = [(1, 3363), (2, 2964), (7, 4249), (11, 2903), (15, 3056),
         (16, 3422), (32, 1172), (35, 1670), (40, 1072)]


def daysToFuture(Input: list) -> list:
    # starts counting from 0
    ans = len(Input)*[0]
    for i in range(len(Input)-1):
        daysToFuture = 0
        minCaseDiff = 10000000000000
        for j in range(i+1, len(Input)):
            if Input[j][1] < Input[i][1] and Input[i][1]-Input[j][1] < minCaseDiff:
                minCaseDiff = Input[i][1]-Input[j][1]
                daysToFuture = Input[j][0]-Input[i][0]
        ans[i] = daysToFuture
    return ans

def fastDaysToFuture(Input: list) -> list:
    # starts counting from 0
    length=len(input)
    ans = length*[0]

    #O(nlogn)
    AVL = makeAVLTree(Input, 'sorted by number of cases')

    for caseTuple in Input[1:length-1]:             #O(nlogn)
        pred=findPredecessor(caseTuple.date)            #O(logn)
        ans[i]=caseTuple.date-pred.date                 #O(logn)
        AVL.delete(caseTuple.date)                      #O(logn)
    
    # last element will trivially be 0 or undefined
    # or something that suggests it's irrelevant

print(daysToFuture(Input))





