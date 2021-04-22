def correctBrackets(s):
    ans = 0
    balance = 0
    for c in s:
        if c=='(':
            balance+=1
        elif balance==0:
            ans+=1
        else:
            balance-=1
    
    return ans+balance

print(correctBrackets('()()()()()'))
