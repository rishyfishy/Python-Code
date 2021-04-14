import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b,c):
    return a*np.exp(-b*x) + c

x_data = []
y_data_t1 = []
y_data_t2 = []
y_data_t3 = []
y_data_t4 = []

with open("lab3 data Exp2.csv") as data:
    csvReader = csv.reader(data,delimiter = ",")

    i=0
    for row in csvReader:
        # print(row)
        if i>0:
            x_data.append(float(row[0]))
            y_data_t1.append(float(row[1]))
            y_data_t2.append(float(row[2]))
            y_data_t3.append(float(row[3]))
            y_data_t4.append(float(row[4]))
        
        i+=1

# print("Resulting x_data: ", x_data)
# print("Resulting y_data_t1: ", y_data_t1)
    # for i in range(0,2):
    #     print(csvReader[i])

#parameters
T_inf = 0
T_i = 50
rho_fuel = 200 #kg/m^3

plt.scatter(x_data,y_data_t1,label="data")

#Curve Fiting:
popt, pcov = curve_fit(func,x_data,y_data_t1)
print("Experiment 1: ", popt)

# popt, pcov = curve_fit(func,x_data,y_data_t2)
# print("Experiment 2: ", popt)

# popt, pcov = curve_fit(func,x_data,y_data_t3)
# print("Experiment 3: ", popt)

# popt, pcov = curve_fit(func,x_data,y_data_t4)
# print("Experiment 4: ", popt)

x_data = np.array(x_data)

#Dumb For loop to generate fitted curve data
y_data_fit1=[]
for num in x_data:
    # print(num)
    y_data_fit1.append(func(x_data,*popt))


# Convert all x_data, y_data arrays into numpy arrays before plotting
y_data_fit1 = np.array(y_data_fit1)
# popt,pcov = curve_fit(func,x_data,y_data_t1,bounds=(0,[3.,1.,0.5]))
# plt.plot(x_data,y_data_t1,"g--",label='fit: a=%5.3f, b=%5.3f, c=%5.3f'%tuple(popt))

#TEst plots
# plt.plot(x_data,y_data_t1,"r-")
# plt.plot(x_data,y_data_t2,"g-")
# plt.plot(x_data,y_data_t3,"b-")
# plt.plot(x_data,y_data_t4,"m-")
fitPlot = plt.plot(x_data,y_data_fit1,"r-", label="fit: a=%5.3f, b=%5.3f, c=%5.3f"%tuple(popt))

# plt.legend(fontsize=10)

plt.show()
plt.xlabel("x")
plt.ylabel("y")
