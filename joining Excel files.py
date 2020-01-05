# This must be run in Python 3.6 (i.e. where Pandas and an approriate Numpy are running)

import os
import xlrd
import csv

path = "/Users/Joseph/Desktop/Python/TNA/Accessions 2017/Temp/"
count = 0

print("Thinking...")

output_file = open("merged - temp.txt", 'a', newline='')
output = csv.writer(output_file, delimiter="¬")

for file in os.listdir(path):
    count += 1
    filename = path + file # full path and filename must be passed

    print(filename)

    #read the excel
    a_return = xlrd.open_workbook(filename) # open file
    a_return = a_return.sheet_by_index(0) # just take the first sheet

    for rownum in range(a_return.nrows):
        if rownum > 3: # skip the first three rows
            output.writerow(a_return.row_values(rownum))

print("Merge complete.")
print(count + " files merged")

output_file.close()

