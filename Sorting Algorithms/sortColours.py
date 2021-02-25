def sortColors(nums):
# Fill this in.
  zeroes,ones,twos=0,0,0

  for i in nums:
    if i==1:
      ones+=1
    elif i==2:
      twos+=1
    else:
      zeroes+=1

  return zeroes*[0]+ones*[1]+twos*[2]

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]


print("After Sort: ")
print(sortColors(nums))
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
