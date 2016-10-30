import numpy as np
import datetime, csv, requests, os

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

