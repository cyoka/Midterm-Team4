import numpy as np
from netCDF4 import Dataset
import datetime, csv

table = []

years = ["Year"]
month = ["Month"]
day = ["Day"]
tmin_arr = ["T_max"]
tmax_arr = ["T_min"]
tav_arr = ["Precip (mm)"]
prcpcm_arr = ["T_ave"]
prcpmm_arr = ["Precip (cm)"]
relhum = ["rh_ave"]

f = open("11015_10-24-2016.csv", "r")

for line in f:
	row = line.strip().split(",")
	table.append(row)


#lst_T = list(map(list, zip(*lst)))
table = table[7:]

table = list(map(list, zip(*table)))

year_set = table[0]
yearday = table[1]
prcpmm = table[3]
tmin_set = table[7]
tmax_set = table[6]
vp_set = table[8]



print(year_set)
print(yearday)
print(prcpmm)
print(tmin_set)
print(tmax_set)
print(vp_set)

# Get data from https://daymet.ornl.gov/gridded/ from 1980-2015
# Download and unzip the file and all the zip files in its subdirectories
# change the path to wherever the data is on your machine


#print("Starting Up")

#years = ["Year"]
#month = ["Month"]
#day = ["Day"]
#tmin_arr = ["T_max"]
#tmax_arr = ["T_min"]
#tav_arr = ["Precip (mm)"]
#prcpcm_arr = ["T_ave"]
#prcpmm_arr = ["Precip (cm)"]
#relhum = ["rh_ave"]


	#relhum.extend((vp_set/(np.exp(((2.453*10**6)/461)*((1/273)-1/(tav_set+273))*6.11))*100))



#print("Creating matrix of values")

#lst = [years, month, day, tmax_arr, tmin_arr, prcpmm_arr, tav_arr, prcpcm_arr, relhum]
#lst_T = list(map(list, zip(*lst)))

#print("Writing into output.csv")

#with open("output.csv", "w") as f:
#    writer = csv.writer(f)
#    writer.writerows(lst_T)

#print("Done!")
