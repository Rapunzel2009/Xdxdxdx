import csv
import math
import statistics
with open("class1.csv",newline="")as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
data = []
for i in range(0,len(fileData)) :
    data.append(int(fileData[i][1]))
#print(data)
total = 0
for i in data :
    total = total + i

mean = total/len(data)
print("mean is", mean)
print("mean is", statistics.mean(data))

squarelist = []
for i in data:
    ans = i-mean
    ans = ans**2
    squarelist.append(ans)

print(squarelist)
squaredsum = 0
for i in squarelist:
    squaredsum = squaredsum+i

result = squaredsum/len(squarelist)

standardDeviation = math.sqrt(result)
print(standardDeviation)
print(statistics.stdev(data))