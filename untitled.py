import matplotlib.pyplot as plt

n=10000
mod=100
lst=n*[0]
sum=0
for i in range(n):
    if i%mod==0:
        sum+=i+1
    else: 
        sum+=1
    lst[i]=sum/(i+1)
plt.plot(lst)
plt.show()