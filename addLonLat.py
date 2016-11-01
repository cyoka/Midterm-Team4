import os, csv

path = "./MoLS-data/"
files = os.listdir(path)

for fname in files:
	if ".csv" in fname:
		lonlat = fname[:-4].split("_")
		lat = float(lonlat[0])
		lon = float(lonlat[1])

		f = open(path+fname, "r")

		table = []

		for line in f:
			table.append(line.strip().split(","))

		for i in range(len(table)):
			table[i].append(lat)
			table[i].append(lon)

	with open(path+fname, "w") as f:
			writer = csv.writer(f)
			writer.writerows(table)
