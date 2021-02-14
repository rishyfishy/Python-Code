
def buddyStrings(A, B):
  # Fill this in.
  if len(A)!=len(B):
    return False
  badList=[]
  for i in range(len(A)):
    if A[i]!=B[i]:
      badList.append(i)
      # if len(badList)==3:
      #   return False
  if len(badList)!=2:
    return False
  elif ((A[badList[0]]==B[badList[1]]) and( A[badList[1]]==B[badList[0]])):
    return True

print (buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print (buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
