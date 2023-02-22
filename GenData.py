import random

# create a list of 500 points
coordinates = []

for coord in range(200):
 x1 = round(random.uniform(-7.1650,-6.4700),4)
 y1 = round(random.uniform(52.8320,53.4670),4)
 x2 = round(random.uniform(-7.0510,-7.0680),4) 
 y2 = round(random.uniform(53.1800,53.1960),4)

 point1 = [x1,y1]
 point2 = [x2,y2]
 
 coordinates.append(point1)
 coordinates.append(point2)

# open a geojson file to add the points to
# change the path to suit your setup

f = open("/Users/ajits1/leafmap/points.geojson", "w")


# opening bracket
f.write('[')

count = 1

# add data to the geojson file (formatted)
for coord in coordinates:
 if count == 1:
  f.write('{\n \
  \t"type": "Feature",\n \
  \t"geometry": {\n \
  \t\t"type": "Point",\n \
  \t\t"coordinates": [' + str(coord[0]) + ',' + str(coord[1]) + ']\n \
  \t}\n \
  }')
 
  count = count + 1
 
 else:
  f.write(',{\n \
  \t"type": "Feature",\n \
  \t"geometry": {\n \
  \t\t"type": "Point",\n \
  \t\t"coordinates": [' + str(coord[0]) + ',' + str(coord[1]) + ']\n \
  \t}\n \
  }')
 
  count = count + 1

# closing bracket
f.write(']')
# close the file
f.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("/Users/ajits1/leafmap/heat_points.js", "w")
# create a variable
f2.write('var heat_points = [')

count = 1

# write data to js file
for coord in coordinates:
 if count == 1:
#  f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')
   f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ',' + str(random.random()) +  ']')

   count = count + 1
 
 else:
#  f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')
   f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ',' + str(random.random()) + ']')

   count = count + 1
# closing bracket
f2.write(']')
# close file
f2.close()