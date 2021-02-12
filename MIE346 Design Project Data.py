# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
resistorString='''
1.0 10 100 1.0K 10K 100K 1.0M
1.1 11 110 1.1K 11K 110K 1.1M
1.2 12 120 1.2K 12K 120K 1.2M
1.3 13 130 1.3K 13K 130K 1.3M
1.5 15 150 1.5K 15K 150K 1.5M
1.6 16 160 1.6K 16K 160K 1.6M
1.8 18 180 1.8K 18K 180K 1.8M
2.0 20 200 2.0K 20K 200K 2.0M
2.2 22 220 2.2K 22K 220K 2.2M
2.4 24 240 2.4K 24K 240K 2.4M
2.7 27 270 2.7K 27K 270K 2.7M
3.0 30 300 3.0K 30K 300K 3.0M
3.3 33 330 3.3K 33K 330K 3.3M
3.6 36 360 3.6K 36K 360K 3.6M
3.9 39 390 3.9K 39K 390K 3.9M
4.3 43 430 4.3K 43K 430K 4.3M
4.7 47 470 4.7K 47K 470K 4.7M
5.1 51 510 5.1K 51K 510K 5.1M
5.6 56 560 5.6K 56K 560K 5.6M
6.2 62 620 6.2K 62K 620K 6.2M
6.8 68 680 6.8K 68K 680K 6.8M
7.5 75 750 7.5K 75K 750K 7.5M
8.2 82 820 8.2K 82K 820K 8.2M
9.1 91 910 9.1K 91K 910K 9.1M
'''
resistorsList=resistorString.split()


# %%

def formatList(lst):        
    for i in range(len(resistorsList)):
        if lst[i][-1]=="K":
            lst[i]= float(lst[i][:-1])*1000
        elif lst[i][-1]=="M":
            lst[i]= float(lst[i][:-1])*1000000
        elif lst[i][-1]=="m":
            lst[i]= float(lst[i][:-1])*0.001
        elif lst[i][-1]=="μ":
            lst[i]= float(lst[i][:-1])*0.000001
        elif lst[i][-1]=="ν":
            lst[i]= float(lst[i][:-1])*0.000000001
        elif lst[i][-1]=="p":
            lst[i]= float(lst[i][:-1])*0.000000000001
        else:
            lst[i]= float(lst[i])
    lst.sort()
    return lst
formatList(resistorsList)
# %%
