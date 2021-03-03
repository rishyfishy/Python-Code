import math
import matplotlib.pyplot as plt
n = 50000
myList=n*[0]
largestPower = math.floor(math.log(n)/math.log(2))
powersOfTwo = {2**b for b in range(1, largestPower+1)}
myDict={0:1}

for i in range(1, n+1):
    sum=(i-1)*myDict[i-1]
    if (i in powersOfTwo):
        sum+=2*i+1
    else:
        sum+=1
    myDict[i]=sum/i

for j in range(n):
    myList[j]=myDict[j+1]
plt.plot(myList)
plt.show()