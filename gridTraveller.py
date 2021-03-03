# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
grids={}
def gridTraveller(m,n):
    if m==0 or n==0:
        return 0
    if m==1 or n==1:
        return 1
    if (m,n) in grids:
        return grids[(m,n)]
    else:
        paths = gridTraveller(m,n-1)+gridTraveller(m-1,n)
        grids[(m,n)]=paths
        grids[(n,m)]=paths
        return paths


# %%
def slowGridTraveller(m,n):
    if m==0 or n==0:
        return 0
    if m==1 or n==1:
        return 1
    return slowGridTraveller(m,n-1)+slowGridTraveller(m-1,n)


# %%
import time
start=time.time()
print(slowGridTraveller(15,15))
print(time.time()-start)


# %%
grids={}
start=time.time()
print(gridTraveller(1000,1000))
print(time.time()-start)


# %%
def fact(n):
    if n==1 or n==2:
        return n
    ans=1
    for i in range(2,n+1):
        ans*=i
    return ans

def fastGridTraveller(m,n):
    sum=m+n
    return fact(sum-2)//(fact(m-1)*fact(n-1))


# %%
grids={}
start=time.time()
print(fastGridTraveller(1000,1000))
print(time.time()-start)


# %%



