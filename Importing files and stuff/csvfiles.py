import csv


x_data = []
y_data_t1 = []
y_data_t2 = []
y_data_t3 = []
y_data_t4 = []
with open("Q2.csv") as data:
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