#======================================= IMPORTS ========================================
import numpy as np
import matplotlib.pyplot as plt
import time 
from scipy.stats import norm
from math import *

#Start the clock in the script to determine computational time.
start_time = time.time()


#======================================= DATA IMPORT ====================================


def import_data(index):
    #List containing all delay files considered.
    file_list = ['20160501.txt', '20160601.txt','20160701.txt', '20160801.txt', '20160901.txt', '20161001.txt','20161101.txt', '20161201.txt', '20172302.txt']

    #Obtain the file name form the file list.
    filename = file_list[index]

    #Generate a matrix with all data in different columns (string format).
    raw_data = np.genfromtxt(filename, dtype='string', delimiter=';')

    #Determine the title for the plots: day, month, year. 
    plot_title = filename[6:8] + '-' + filename[4:6] + '-' + filename[:4]
    return raw_data, plot_title

#obtain the raw data
#raw_data, plot_title = import_data(0)
raw_data1, plot_title1 = import_data(2)
#raw_data2, plot_title2 = import_data(7)
#raw_data3, plot_title3 = import_data(8)

fileicao = 'ICAO.csv'

icaodata = np.genfromtxt(fileicao, dtype='string', delimiter=';')
icaodatastr = []

for i in range(len(icaodata)):
    icaodatastr.append(icaodata[i].split(","))


#======================================= FILTER 1 =======================================


###Generate a new list which will houshold the european flights.
##data_filter = []
##
##for i in range(len(raw_data)):
##    #All european airports have an ICAO code startign eahter with an 'E' (north) or 'L'
##    #(south). This loop ignores all non-european flights (i.e. departure/arrival outside
##    #EU). European fights are added to a new data list.
##    
##    if raw_data[i][0][:1] == 'E' or raw_data[i][0][:1] == 'L' or raw_data[i][0][:2] == 'UG' or raw_data[i][0][:2] == 'UB' or raw_data[i][0][:2] == 'UK':
##        if raw_data[i][1][:1] == 'E' or raw_data[i][1][:1] == 'L' or raw_data[i][1][:2] == 'UG' or raw_data[i][1][:2] == 'UB' or raw_data[i][1][:2] == 'UK':
##            data_filter.append(raw_data[i])
##        else:
##            continue
##    else:
##        continue
##
###Convert the list with european flights to an array.
##data = np.asarray(data_filter)


#Generate a new list which will houshold the european flights.
data_filter1 = []

for i in range(len(raw_data1)):
    #All european airports have an ICAO code startign eahter with an 'E' (north) or 'L'
    #(south). This loop ignores all non-european flights (i.e. departure/arrival outside
    #EU). European fights are added to a new data list.
    
    if raw_data1[i][0][:1] == 'E' or raw_data1[i][0][:1] == 'L' or raw_data1[i][0][:2] == 'UG' or raw_data1[i][0][:2] == 'UB' or raw_data1[i][0][:2] == 'UK':
        if raw_data1[i][1][:1] == 'E' or raw_data1[i][1][:1] == 'L' or raw_data1[i][1][:2] == 'UG' or raw_data1[i][1][:2] == 'UB' or raw_data1[i][1][:2] == 'UK':
            data_filter1.append(raw_data1[i])
        else:
            continue
    else:
        continue

#Convert the list with european flights to an array.
data1 = np.asarray(data_filter1)

##
###Generate a new list which will houshold the european flights.
##data_filter2 = []
##
##for i in range(len(raw_data2)):
##    #All european airports have an ICAO code startign eahter with an 'E' (north) or 'L'
##    #(south). This loop ignores all non-european flights (i.e. departure/arrival outside
##    #EU). European fights are added to a new data list.
##    
##    if raw_data2[i][0][:1] == 'E' or raw_data2[i][0][:1] == 'L' or raw_data2[i][0][:2] == 'UG' or raw_data2[i][0][:2] == 'UB' or raw_data2[i][0][:2] == 'UK':
##        if raw_data2[i][1][:1] == 'E' or raw_data2[i][1][:1] == 'L' or raw_data2[i][1][:2] == 'UG' or raw_data2[i][1][:2] == 'UB' or raw_data2[i][1][:2] == 'UK':
##            data_filter2.append(raw_data2[i])
##        else:
##            continue
##    else:
##        continue
##
###Convert the list with european flights to an array.
##data2 = np.asarray(data_filter2)
##
##
###Generate a new list which will houshold the european flights.
##data_filter3 = []
##
##for i in range(len(raw_data3)):
##    #All european airports have an ICAO code startign either with an 'E' (north) or 'L'
##    #(south). This loop ignores all non-european flights (i.e. departure/arrival outside
##    #EU). European fights are added to a new data list.
##    
##    if raw_data3[i][0][:1] == 'E' or raw_data3[i][0][:1] == 'L' or raw_data3[i][0][:2] == 'UG' or raw_data3[i][0][:2] == 'UB' or raw_data3[i][0][:2] == 'UK':
##        if raw_data3[i][1][:1] == 'E' or raw_data3[i][1][:1] == 'L' or raw_data3[i][1][:2] == 'UG' or raw_data3[i][1][:2] == 'UB' or raw_data3[i][1][:2] == 'UK':
##            data_filter3.append(raw_data3[i])
##        else:
##            continue
##    else:
##        continue
##
###Convert the list with european flights to an array.
##data3 = np.asarray(data_filter3)


#======================================= FILTER 2 =======================================


#Open the file which contains all common types of helicopters.
helicopter_data = np.genfromtxt('helicopterdata.txt', dtype='string', delimiter=';')

###Generate a new list which will houshold all non-helicopter flights.
##data_filter = []
##
##for i in range(len(data)):
##    #The original data array contains the aircraft type in the fourth column.
##    #The code checks if this particular aircraft found in the data corresponds
##    #to one of the entries in the elicopter data file. If the parcticular aircraft
##    #is not in the helicopter file (i.e. no helicopter), the list is appended.
##    if data[:,3][i] in helicopter_data:
##        continue
##    else:
##        data_filter.append(data[i])
##        
###Convert the 'data_filter' list to an array and overwrite the old 'data' list.
##data = np.asarray(data_filter)


#Generate a new list which will houshold all non-helicopter flights.
data_filter1 = []

for i in range(len(data1)):
    #The original data array contains the aircraft type in the fourth column.
    #The code checks if this particular aircraft found in the data corresponds
    #to one of the entries in the elicopter data file. If the parcticular aircraft
    #is not in the helicopter file (i.e. no helicopter), the list is appended.
    if data1[:,3][i] in helicopter_data:
        continue
    else:
        data_filter1.append(data1[i])
        
#Convert the 'data_filter' list to an array and overwrite the old 'data' list.
data1 = np.asarray(data_filter1)

###Generate a new list which will houshold all non-helicopter flights.
##data_filter2 = []
##
##for i in range(len(data2)):
##    #The original data array contains the aircraft type in the fourth column.
##    #The code checks if this particular aircraft found in the data corresponds
##    #to one of the entries in the elicopter data file. If the parcticular aircraft
##    #is not in the helicopter file (i.e. no helicopter), the list is appended.
##    if data2[:,3][i] in helicopter_data:
##        continue
##    else:
##        data_filter2.append(data2[i])
##        
###Convert the 'data_filter' list to an array and overwrite the old 'data' list.
##data2 = np.asarray(data_filter2)
##
##
###Generate a new list which will houshold all non-helicopter flights.
##data_filter3 = []
##
##for i in range(len(data3)):
##    #The original data array contains the aircraft type in the fourth column.
##    #The code checks if this particular aircraft found in the data corresponds
##    #to one of the entries in the elicopter data file. If the parcticular aircraft
##    #is not in the helicopter file (i.e. no helicopter), the list is appended.
##    if data3[:,3][i] in helicopter_data:
##        continue
##    else:
##        data_filter3.append(data3[i])
##        
###Convert the 'data_filter' list to an array and overwrite the old 'data' list.
##data3 = np.asarray(data_filter3)

#======================================= FILTER 3 =======================================


#Open the file which contains all common types of helicopters.
military_data = np.genfromtxt('militarydata.txt', dtype='string', delimiter=';')

###Generate a new list which will houshold all non-military flights.
##data_filter = []
##
##for i in range(len(data)):
##    #This filter works exactly the same as the helicopter filter, only now
##    #military aircraft are removed from the dataset. Also unknown aircraft are
##    #removed (these have a 'zzzz' marking).
##    if data[:,3][i] in military_data:
##        continue
##    else:
##        data_filter.append(data[i])
##        
###Convert the 'data_filter' list to an array and overwrite the old 'data' list.
##data = np.asarray(data_filter)


#Generate a new list which will houshold all non-military flights.
data_filter1 = []

for i in range(len(data1)):
    #This filter works exactly the same as the helicopter filter, only now
    #military aircraft are removed from the dataset. Also unknown aircraft are
    #removed (these have a 'zzzz' marking).
    if data1[:,3][i] in military_data:
        continue
    else:
        data_filter1.append(data1[i])
        
#Convert the 'data_filter' list to an array and overwrite the old 'data' list.
data1 = np.asarray(data_filter1)


###Generate a new list which will houshold all non-military flights.
##data_filter2 = []
##
##for i in range(len(data2)):
##    #This filter works exactly the same as the helicopter filter, only now
##    #military aircraft are removed from the dataset. Also unknown aircraft are
##    #removed (these have a 'zzzz' marking).
##    if data2[:,3][i] in military_data:
##        continue
##    else:
##        data_filter2.append(data2[i])
##        
###Convert the 'data_filter' list to an array and overwrite the old 'data' list.
##data2 = np.asarray(data_filter2)
##
##
###Generate a new list which will houshold all non-military flights.
##data_filter3 = []
##
##for i in range(len(data3)):
##    #This filter works exactly the same as the helicopter filter, only now
##    #military aircraft are removed from the dataset. Also unknown aircraft are
##    #removed (these have a 'zzzz' marking).
##    if data3[:,3][i] in military_data:
##        continue
##    else:
##        data_filter3.append(data3[i])
##        
###Convert the 'data_filter' list to an array and overwrite the old 'data' list.
##data3 = np.asarray(data_filter3)

#SOURCES:
# https://contentzone.eurocontrol.int/aircraftperformance/default.aspx?GroupFilter=5
# https://en.wikipedia.org/wiki/List_of_ICAO_aircraft_type_designators


#======================================= FILTER 4 =======================================


###Remove airport if the total amount of deperatures is less than the threshold.
##airport_remove_threshold = 0
##
##unique_airport, unique_airport_count = np.unique(data[:,0], return_counts=True)
##
##unique_airport_filter = []
##for i in range(len(unique_airport)):
##    if unique_airport_count[i] < airport_remove_threshold:
##        continue
##    else:
##        unique_airport_filter.append(unique_airport[i])
##unique_airport = np.asarray(unique_airport_filter)
##
##data_filter = []
##for i in range(len(data)):
##    if data[:,0][i] in unique_airport:
##        data_filter.append(data[i])
##    else:
##        continue
##data = np.asarray(data_filter)
##
##unique_airport, unique_airport_count = np.unique(data[:,0], return_counts=True)
##
###Determine the amount of entries eliminated in this filter.
##elm_filter_4 = len(raw_data)-len(data)-elm_filter_1-elm_filter_2-elm_filter_3


#======================================= CLUSTER DATA ===================================


#Cluster departure/arrival airport, aircraft type, flightnumber and carrier.
#Arrays contain string data.
##departure_airport = data[:,0]
##arrival_airport = data[:,1]
##airport = data[:,3]

#for i in range(len(airport)):
    #if airport[


##x = np.arange(20376)
##dis = []
##
##for i in xrange(len(departure_airport)):
##    for j in xrange(len(icaodatastr)):
##        if departure_airport[i] == icaodatastr[j][5]:
##            for k in xrange(len(icaodatastr)):
##                if arrival_airport[i] == icaodatastr[k][5]:
##                    dep_lat = eval(icaodatastr[j][6])
##                    dep_lon = eval(icaodatastr[j][7])
##                    arr_lat = eval(icaodatastr[k][6])
##                    arr_lon = eval(icaodatastr[k][7])
##
##                    e = pi*dep_lat/180
##                    f = pi*dep_lon/180
##                    g = pi*arr_lat/180
##                    h = pi*arr_lon/180
##
##                    R = 6378
##
##                    lim = cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)
##
##                    if lim >= -1 and lim <= 1: 
##                        dis.append(R*acos(cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)))
##                    else:
##                        dis.append(0)
##                else:
##                    dep_lat = 0
##                    dep_lon = 0
##                    arr_lat = 0
##                    arr_lon = 0
##        else:
##            continue
##
##threshold = 0.0
##set_threshold = []
##xlst = []
##i = 0
##
##dis.sort()
##
##while threshold <= 1.0:
##    xlst.append(i)
##    set_threshold.append(dis[int(len(dis)*threshold)])
##    threshold += 0.01
##    i += 1


#Cluster departure/arrival airport, aircraft type, flightnumber and carrier.
#Arrays contain string data.
departure_airport1 = data1[:,0]
arrival_airport1 = data1[:,1]
x1 = np.arange(20376)
dis1 = []
count = []

for i in xrange(len(departure_airport1)):
    for j in xrange(len(icaodatastr)):
        if departure_airport1[i] == icaodatastr[j][5]:
            for k in xrange(len(icaodatastr)):
                if arrival_airport1[i] == icaodatastr[k][5]:
                    dep_lat = eval(icaodatastr[j][6])
                    dep_lon = eval(icaodatastr[j][7])
                    arr_lat = eval(icaodatastr[k][6])
                    arr_lon = eval(icaodatastr[k][7])

                    e = pi*dep_lat/180
                    f = pi*dep_lon/180
                    g = pi*arr_lat/180
                    h = pi*arr_lon/180

                    R = 6378

                    lim = cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)

                    if lim >= -1 and lim <= 1:
                        distance = R*acos(cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g))
                        dis1.append(distance)
                        if distance < 994:
                            count.append(distance)
                    else:
                        dis1.append(0)
                else:
                    dep_lat = 0
                    dep_lon = 0
                    arr_lat = 0
                    arr_lon = 0
        else:
            continue

dis1.sort()
threshold = 0.0
set_threshold1 = []
xlst1 = []
i = 0

dis1.sort()

while threshold <= 1.0:
    xlst1.append(i)
    set_threshold1.append(dis1[int(len(dis1)*threshold)])
    threshold += 0.01
    i += 1

print(dis1[int(len(dis1)*0.9)])

##
###Cluster departure/arrival airport, aircraft type, flightnumber and carrier.
###Arrays contain string data.
##departure_airport2 = data2[:,0]
##arrival_airport2 = data2[:,1]
##x2 = np.arange(20376)
##dis2 = []
##
##for i in xrange(len(departure_airport2)):
##    for j in xrange(len(icaodatastr)):
##        if departure_airport2[i] == icaodatastr[j][5]:
##            for k in xrange(len(icaodatastr)):
##                if arrival_airport2[i] == icaodatastr[k][5]:
##                    dep_lat = eval(icaodatastr[j][6])
##                    dep_lon = eval(icaodatastr[j][7])
##                    arr_lat = eval(icaodatastr[k][6])
##                    arr_lon = eval(icaodatastr[k][7])
##
##                    e = pi*dep_lat/180
##                    f = pi*dep_lon/180
##                    g = pi*arr_lat/180
##                    h = pi*arr_lon/180
##
##                    R = 6378
##
##                    lim = cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)
##
##                    if lim >= -1 and lim <= 1: 
##                        dis2.append(R*acos(cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)))
##                    else:
##                        dis2.append(0)
##                else:
##                    dep_lat = 0
##                    dep_lon = 0
##                    arr_lat = 0
##                    arr_lon = 0
##        else:
##            continue
##
##threshold = 0.0
##set_threshold2 = []
##xlst2 = []
##i = 0
##
##dis2.sort()
##
##while threshold <= 1.0:
##    xlst2.append(i)
##    set_threshold2.append(dis2[int(len(dis2)*threshold)])
##    threshold += 0.01
##    i += 1


#Cluster departure/arrival airport, aircraft type, flightnumber and carrier.
#Arrays contain string data.
##departure_airport3 = data3[:,0]
##arrival_airport3 = data3[:,1]
##x3 = np.arange(20376)
##dis3 = []
##
##for i in xrange(len(departure_airport3)):
##    for j in xrange(len(icaodatastr)):
##        if departure_airport3[i] == icaodatastr[j][5]:
##            for k in xrange(len(icaodatastr)):
##                if arrival_airport3[i] == icaodatastr[k][5]:
##                    dep_lat = eval(icaodatastr[j][6])
##                    dep_lon = eval(icaodatastr[j][7])
##                    arr_lat = eval(icaodatastr[k][6])
##                    arr_lon = eval(icaodatastr[k][7])
##
##                    e = pi*dep_lat/180
##                    f = pi*dep_lon/180
##                    g = pi*arr_lat/180
##                    h = pi*arr_lon/180
##
##                    R = 6378
##
##                    lim = cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)
##
##                    if lim >= -1 and lim <= 1: 
##                        dis3.append(R*acos(cos(e)*cos(g)*cos(h - f) + sin(e)*sin(g)))
##                    else:
##                        dis3.append(0)
##                else:
##                    dep_lat = 0
##                    dep_lon = 0
##                    arr_lat = 0
##                    arr_lon = 0
##        else:
##            continue
##
##threshold = 0.0
##set_threshold3 = []
##xlst3 = []
##i = 0
##
##dis3.sort()
##
##while threshold <= 1.0:
##    xlst3.append(i)
##    set_threshold3.append(dis3[int(len(dis3)*threshold)])
##    threshold += 0.01
##    i += 1

##def rollingavg(dis,x):
##    #returns rolling averages in a list, and the time at which the last value of the average
##    #was obtained.
##    #vlist contains values, tlist contains the times at which values are measured
##    #N is the stepsize, S is the amount of previous terms that need to be averaged
##    #S should be equal to or greater than N to prevent a loss of information
##
##    avg=[]
##    condition=True
##    i=1
##    while condition:
##        
##        #on the first couple iterations, only use numbers actually in list (start from zero)
##        if (i - 1)<0:
##            avg.append(sum(dis[0:(i)])/float(1*i))
##        else:
##            avg.append(sum(dis[(i - 1):(i)])/float(1))
###debug           
###        print avg
###        raw_input()
##            
##        #Stop at the end of the list (excludes the final X terms;  X<N)
##        if (i+1) > len(dis):
##            condition = False
##        i+=1
##    return avg
##
##rolavg = rollingavg(dis,x)

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

###plt.plot(xlst,set_threshold, label="May '16")
##plt.plot(xlst1,set_threshold1, label="August '16")
###plt.plot(xlst2,set_threshold2, label="December '16")
###plt.plot(xlst3,set_threshold3, label="Februari '17")
##plt.axvline(90, linestyle="dashed", color="Red",label="Threshold")
##plt.xlabel("% of flights")
##plt.ylabel("range [km]")
##ax = plt.subplot(111)
##box = ax.get_position()
##ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
##ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
##plt.grid()
##plt.show()

ax = plt.subplot(111)
plt.hist(dis1,bins=80)
plt.xlabel("range [km]")
plt.ylabel("number of flights [-]")
ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.grid()
plt.show()

#lst = [1879.3,1952.9,1761.6,1854,1789.6,2003,1541.4,1537.9,1617.7]


