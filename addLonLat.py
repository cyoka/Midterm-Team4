import os

path = "./MoLS-master/test_data/"
files = listdir(path)

for fname in files:
	if ".csv" in fname:
		lonlat = fname[:-4].split("_")
		lat = float(lonlat[0])
		lon = float(lonlat[1])

		f = open(path+fname, "r")

		table = []

		for line in f:
			if len(line)==0:
				continue
			else:
				table.append(line.strip().split(","))

		table[0].append("lat")
		table[0].append("lon")
		for i in range(1, len(table)):
			table[i].append(lat)
			table[i].append(lon)

	with open(path+fname, "w") as f:
			writer = csv.writer(f)
			writer.writerows(lst_T)
