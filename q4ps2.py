lst = []
listofDiffs = []
for i in range(len(lst)-1):
      country = lst[i][2]
      year = lst[i][0]
      maxdiffyears = 0
      for j in range(i=1, len(lst)):
            if lst[j][2] = country:
                  maxdiffyears = year-lst[j][0]
      listofDiffs.append((maxdiffyears, country)

findmax(maxdiffyears), return its country

mydict={}  # implemented in a hashmap, searches are O(1)
lst=[]
maxdiffyears=0
for i in range(len(lst)):  # O(n)
      if lst[i][2] in mydict:
            if (mydict[lst[i][2]].value-lst[i][0] > maxdiffyears):
                  maxdiffyears=mydict[lst[i][2]].value-lst[i][0]
                  bestCountry=lst[i][2]
      else:
          mydict[lst[i][2]]=lst[i][0]
