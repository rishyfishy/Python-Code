def num2cell(num:int)->str:
    if num<1:
        return ""
    elif num<27:
        return chr(num+64)
    else:
        a=(num-1)//26
        return num2cell(a)+num2cell(num-26*a)

# print(num2cell(27+26))
# print(num2cell(51))
# print(num2cell(52))
# print(num2cell(676))
# print(num2cell(702))
# print(num2cell(704))
# print(num2cell(456976))
