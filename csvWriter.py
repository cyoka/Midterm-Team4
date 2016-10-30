import numpy as np
import datetime, csv, requests, os

#coordinates for your city, one upper left, one bottom right(set to flagstaff)
"""
ul = (32.2299,-110.9183)
br = (32.2389,-110.9093)
years =  "1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015"
#the number of steps in the lat/lon difference, we rounded up to make sure 
# we would not step over any square kilometers.
latStep = 15
lonStep = 20

#the change in lat and lon values, for incrementing
deltaLat = (ul[0]-br[0])/latStep
deltaLon = (ul[1]-br[1])/lonStep

# Setup the request url and parameters
url = 'https://daymet.ornl.gov/data/send/saveData'
# these values are passed along as parameters in the 
# http request 
payload = {
		'lat':br[0],
		'lon':br[1],
		'year':years,
	}
# create a directory for the downloaded data
dataDir = "daymetData";
if not os.path.exists('daymetData'):
	os.makedirs('daymetData')

Loop through the grid of lat,lon to get all of the 1km^2 daymet csvs


for latitude in range(0,latStep):
	for longitude in range(0,lonStep):
		# Get the first and last year and build a string in formay yyyy-yyyy for creating a filename
		# prepend lat-lon to the filename 
		filenameYears = payload['year'].split(',')
		filename = str(payload['lat'])+'_'+str(payload['lon'])+'_'+filenameYears[0]+'-'+filenameYears[-1]
		if os.path.isfile(dataDir+'/'+filename):
			print("File "+dataDir+'/'+filename+" already exists.")
		else:
			csvFile = requests.get(url, params=payload)
			
			print("Writing to "+dataDir+'/'+filename)
			#create the new csv
		
			f = open(dataDir+'/'+filename,'w')
			#write the csv
			print(csvFile.text,file = f)

			f.close()

			print("Starting conversions")
"""

files = os.listdir("./initial-data")

for fname in files:
	if ".csv" in fname:
		lonlat = fname[:-4].split("_")
		lat = float(lonlat[0])
		lon = float(lonlat[1])

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

		f = open("./initial-data/"+fname, 'r')

		for line in f:
			if len(line)==0:
				continue
			elif line[0] not in ['1', '2']:
				continue
			else:
				row = line.strip().split(",")
				table.append(row)

		if len(table)==0:
			print('table is empty')

		table = list(map(list, zip(*table)))

		year_set = [int(numeric_string) for numeric_string in table[0]]
		yearday = [int(numeric_string) for numeric_string in table[1]]
		prcpmm = [float(numeric_string) for numeric_string in table[2]]
		tmin_set = [float(numeric_string) for numeric_string in table[4]]
		tmax_set = [float(numeric_string) for numeric_string in table[3]]
		vp_set = [float(numeric_string) for numeric_string in table[5]]


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



		with open("./parsed_data/"+fname, "w") as f:
			writer = csv.writer(f)
			writer.writerows(lst_T)


			#System calls to generate Jocelines files. DEPENDENT ON FILE LOCATIONS
			#os.system("mv "+dataDir+'/'+filename+ " ./MoLS/Weather/")
			
			#os.system("python ./MoLS/Run_Model.py")

		#payload['lon'] += deltaLon #increment longitude
	#payload['lon'] = br[1] #reset latitude
	#payload['lat'] += deltaLat #increment latitude
