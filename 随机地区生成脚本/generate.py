import geopy
from geopy.distance import geodesic
import random
import urllib.request
import json

# 获取文本输入数据
print("读取输入信息")
lat = []
lon = []
distance = []
goal = []
inputFileName = 'input.txt'
with open(inputFileName) as inputLocations:
    for inputLocation in inputLocations:
        inputInformation = inputLocation.split(" ")
        lon.append(float(inputInformation[0]))
        lat.append(float(inputInformation[1]))
        distance.append(float(inputInformation[2]))
        goal.append(int(inputInformation[3]))

# 计算每个地区要生成的数量
inputLineNumber = len(lat)
k = 1.5
goalGenerate = []
for i in range(inputLineNumber):
    goalGenerate.append(int(goal[i]*k))

# 计算每个地区周边生成的地区
d = geodesic((0.0,0.0), (30.0,120.0))
points = {}
for i in range(inputLineNumber):
    start = geopy.Point(lat[i],lon[i])
    points[i] = []
    for j in range(goalGenerate[i]):
        bearing = random.random()*360
        distanceGenerate = random.random()*distance[i]
        points[i].append(d.destination(start, bearing, distanceGenerate))

# 合并网址，并访问获取响应信息
responses = {}
print("合成访问接口字符串并获取响应信息")
print("访问地区数:"+str(inputLineNumber))
for i in range(inputLineNumber):
    responses[i] = []
    for j in range(goalGenerate[i]):
        part1 = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'
        part2 = str(points[i][j].longitude)
        part3 = ','
        part4 = str(points[i][j].latitude)
        part5 = '.json?access_token=pk.eyJ1IjoiamlqaWZlbmciLCJhIjoiY2trYmJ5ZDZwMG9lODJ1cjF5ZG4zb2U4YiJ9.yQ09Rtl2qgyM2YtXbf-wjA';
        url = part1+part2+part3+part4+part5
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        response = resp.read().decode('utf-8')
        responses[i].append(response)
    print("已处理地区:" + str(i+1))

# 获取最终结果信息并写入output
print("将地区信息存入output.txt")
outputFileName = 'output.txt'
with open(outputFileName, 'a') as output:
    output.truncate(0)
    for i in range(inputLineNumber):
        count = 0
        for j in range(goalGenerate[i]):
            if count < goal[i]:
                jsonString = responses[i][j]
                jsonDict = json.loads(jsonString)
                allPlaceInOneJson = jsonDict['features']
                if len(allPlaceInOneJson) != 0:
                    firstPlcaeInOneJson = allPlaceInOneJson[0]
                    coordinates = firstPlcaeInOneJson['geometry']['coordinates']
                    place = firstPlcaeInOneJson['place_name']
                    output.write(str(coordinates[1]) + "," + str(coordinates[0]))
                    output.write("\t")
                    output.write(place)
                    output.write("\n")
                    count = count + 1

# 获取乱序结果信息并写入output_random
print("将无序地区信息存入output_random.txt")
outputRandomFileName = 'output_random.txt'
locatiionList = []
with open(outputFileName) as locations:
    for location in locations:
        locatiionList.append(location)

random.shuffle(locatiionList)

with open(outputRandomFileName, 'a') as output:
    output.truncate(0)
    for i in range(len(locatiionList)):
        output.write(locatiionList[i])

print("运行完成")


