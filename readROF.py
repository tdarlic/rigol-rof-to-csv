#!/use/bin/python3.5

import sys
import struct

filename = sys.argv[1]

print("Checking: " + filename)

file = open(filename, "rb")
fileContent = file.read()

fileHeader = struct.unpack("<cccccchIhhIII", fileContent[:28])

#print(str(fileHeader))
sample_period = fileHeader[10]
num_points = fileHeader[11]
print("Sample period: " + str(sample_period))
print("Number of points: " + str(num_points))
print("Timspan: " + str(num_points * sample_period) + " seconds")
print("CH1-Vol,CH1-Cur,CH2-Vol,CH2-Cur,CH3-Vol,CH3-Cur")

data = struct.unpack("<" + ("iiiiii" * (num_points)), fileContent[28:])

icnt = 0

for i in data:
    if (icnt < 5):
        print(str(i/10000), end = ",")
        icnt = icnt + 1
    else:
        print(str(i/10000))
        icnt = 0

#print(str(data))
