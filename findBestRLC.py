def omega_c(r,c):
    return 1/(r*c)
res=[100,220,470,680,1000,2000,3900,8200,15000,18000,36000,39000,47000,82000,100000]
cap=[100e-9,220e-9,680e-9,820e-9,1e-6,2.2e-6,4.7e-6,10e-6]

def findBestRC(resistors:list, caps:list, func, target:float):
    best=[resistors[0],caps[0]]
    #ToDo:better error function
    error=abs(func(best[0],best[1])-target)
    #Todo:Tighter code for sorted lists
    for r in resistors:
        for c in caps:
            newError=abs(func(r,c)-target)
            if (newError<error):
                best=[r,c]
                error=newError

    print ("error is "+str(error))
    return best[0],best[1]

bestr,bestc=findBestRC(res,cap,omega_c,12.6)

def RR(r1,r2):
    return r1*r2

def findBestRR(resistors:list, func, target:float):
    best=[resistors[0],resistors[0]]
    #ToDo:better error function
    error=abs(func(best[0],best[1])-target)
    #Todo:Tighter code for sorted lists
    for i in range(len(resistors)-1):
        for j in range(i,len(resistors)): #duplicates allowed
            newError=abs(func(resistors[i],resistors[j])-target)
            if (newError<error):
                best=[resistors[i],resistors[j]]
                error=newError

    print ("error is "+str(error))
    return best[0],best[1]


# %%
targit=1/(632*bestc*bestc)
newr1,newr3=findBestRR(res,RR,targit)
print(newr1,newr3)


# %%



