def par(*args):
    # Resistance of parallel resistors
    # Make sure units are consistent
    prod=1
    for r in args:
        prod*=r
    if not prod:
        return 0
    sum=0
    for r in args:
        sum+=prod/r

    return prod/sum

print(par(1.8,100,20,50))