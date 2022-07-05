# testcsv.py

import csv


def writetocsv():
	with open('data.csv','a',newline='',encodeing='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data)

data = ['Mango',30]
writetocsv(data)