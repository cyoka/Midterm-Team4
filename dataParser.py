import numpy as np
from netCDF4 import Dataset
import datetime, csv

table = []

years = ["Year"]
month = ["Month"]
day = ["Day"]
tmin_arr = ["T_min"]
tmax_arr = ["T_max"]
tav_arr = ["T_ave"]
prcpcm_arr = ["Precip (cm)"]
prcpmm_arr = ["Precip (mm)"]
relhum = ["rh_ave"]

f = open("11015_10-25-2016.csv", "r")

for line in f:
	row = line.strip().split(",")
	table.append(row)

table = table[8:]

table = list(map(list, zip(*table)))

year_set = [int(numeric_string) for numeric_string in table[0]]
yearday = [int(numeric_string) for numeric_string in table[1]]
prcpmm = [float(numeric_string) for numeric_string in table[3]]
tmin_set = [float(numeric_string) for numeric_string in table[7]]
tmax_set = [float(numeric_string) for numeric_string in table[6]]
vp_set = [float(numeric_string) for numeric_string in table[8]]


for j in range(len(yearday)):
	date = datetime.date(year_set[j], 1, 1) + datetime.timedelta(yearday[j]-1)
	month.append(date.month)
	day.append(date.day)

tav_set = (np.asarray(tmax_set)+np.asarray(tmin_set))/2
years.extend(year_set)
tmin_arr.extend(tmin_set)
tmax_arr.extend(tmax_set)
prcpmm_arr.extend(prcpmm)
tav_arr.extend(tav_set)
prcpcm_arr.extend(np.asarray(prcpmm)/10)
relhum.extend(((np.asarray(vp_set))/(np.exp(((2.453*(10**6))/461)*((1/273)-1/(tav_set+273)))*6.11)))

lst = [years, month, day, tmax_arr, tmin_arr, prcpmm_arr, tav_arr, prcpcm_arr, relhum]
lst_T = list(map(list, zip(*lst)))

with open("MoLS_Input.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lst_T)
