def max_subarray_sum(arr):
    # Fill this in.
    sum=0
    for num in arr:
        sum+=num
        if sum<0:
            sum=0
    return sum


print (max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
