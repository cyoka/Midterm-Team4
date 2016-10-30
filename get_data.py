import pandas as pd
import csv
import requests

# intial latitude and longitude values
initial_lat = 32.3094
initial_lon = -111.0625

# roughly 1-km in each direction
lat_step = 0.009
lon_step = 0.106

# how big of an area we want to cover in km
steps = 10

lat = initial_lat
lon = initial_lon

# CSV file header
header = 'Year,Month,Day,T_max,T_min,Precip (mm),T_ave,Precip (cm),rh_ave'
path = './initial-data/'

# loop through all lat/lon values and write csv files
for i in range(steps):
    if i != 0:
        lat -= lat_step
    for j in range(steps):
        if j != 0:
            lon += lon_step
        #print (str(round(lat,4)) + ', ' + str(round(lon,4)))
        data = pd.read_csv('https://daymet.ornl.gov/data/send/saveData?lat=' + str(round(lat,4)) + '&lon=' + str(round(lon,4)) + '&measuredParams=tmax,tmin,prcp,vp',skiprows=7)
        data.to_csv(path + str(round(lat,4)) + '_' + str(round(lon,4)) + '.csv',index=False)
    lon = initial_lon