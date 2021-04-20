def num2cell(num:int)->str:
    if num<1:
        return ""
    elif num<27:
        return chr(num+64)
    else:
        return num2cell(num//27)+num2cell((num+1)%27)

print(num2cell(27))
print(num2cell(27*27))
print(num2cell(27**3))
print(num2cell(27**4))