import numpy as np
from netCDF4 import Dataset
import datetime, csv

print("Starting Up")

years = ["year"]
month = ["month"]
day = ["day"]
tmin_arr = ["tmin"]
tmax_arr = ["tmax"]
tav_arr = ["tav"]
prcpcm_arr = ["prcp (cm)"]
prcpmm_arr = ["prcp (mm)"]
relhum = ["Relative Humidity"]

print("Parsing through .nc files")
for year in range(1980, 2016):
	path = "/Users/CYOka/Desktop/daymet/V3/CF_tarred/tars_" + str(year) + "/11015_" + str(year) + "/"
	tmin = Dataset(path + "tmin.nc", "r")
	tmax = Dataset(path + "tmax.nc", "r")
	vp = Dataset(path + "vp.nc", "r")
	prcp = Dataset(path + "prcp.nc", "r")

	tmin_set = tmin.variables["tmin"][:]
	tmax_set = tmax.variables["tmax"][:]
	vp_set = vp.variables["vp"][:]
	prcp_set = prcp.variables["prcp"][:]
	tav_set = (tmax_set + tmin_set) /2

	i = 0
	while i < 365:
		date = datetime.date(year, 1, 1) + datetime.timedelta(i)
		years.append(year)
		month.append(date.month)
		day.append(date.day)
		i = i+1


	tmin_arr.extend(tmin_set)
	tmax_arr.extend(tmax_set)
	prcpcm_arr.extend(prcp_set/10)
	prcpmm_arr.extend(prcp_set)
	tav_arr.extend(tav_set)
	relhum.extend((vp_set/(np.exp(((2.453*10**6)/461)*(tav_set*(-1))*6.11))*100))

	tmin.close()
	tmax.close()
	vp.close()
	prcp.close()

print("Creating matrix of values")
lst = [years, month, day, tmax_arr, tmin_arr, prcpmm_arr, tav_arr, prcpcm_arr, relhum]
lst_T = list(map(list, zip(*lst)))

print("Writing into .csv file")
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lst_T)

print("Done!")
