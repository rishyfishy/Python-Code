# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import datetime
import csv
import os
newString = '''
    0.8000    1.0000    0.9000    4.7910    0.2485    1.1907   10.0000

    0.9000    1.0000    0.9500    0.2485   -2.7726   -0.6890    0.0526

    0.9000    0.9500    0.9250    0.2485   -1.1915   -0.2961    0.0270

    '''

def cleanDisp(matlabString:str)->None:

    singleSplit = matlabString.split("\n")
    doubleSplit=[x.split(" ") for x in singleSplit]
    filtered=[]
    for line in doubleSplit:
        filtered.append([x for x in line if x])
    filtered
    doubleFiltered = [x for x in filtered if x]

    now = datetime.datetime.now()

    # dd/mm/YYYY H:M
    dt_string = now.strftime("%d-%m-%Y_%H-%M")
    dt_string+=".csv"

    with open(dt_string, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(doubleFiltered)
    
    cwd=os.getcwd()
    csvfile = os.path.join(cwd,dt_string)
    os.startfile(csvfile)
# %%
cleanDisp(newString)