def witnesses(heights):
  # Fill this in.
    numWitnesses=0
    tallest=0
    for i in reversed(range(len(heights))):
        if (heights[i]>tallest):
            numWitnesses+=1
            tallest=heights[i]
    return numWitnesses


print (witnesses([3, 6,3, 4, 4, 1]))
# 3
