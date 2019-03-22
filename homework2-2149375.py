import math

# PART 1
number_of_coordinates = int(input("Please give the number of coordinates: "))
coordinates = []

for coord_index in range(0,number_of_coordinates):
    tuple_string = input()[1:-1]
    tuple_splitted = tuple_string.split(',')
    coordinates.append(( int(tuple_splitted[0]), int(tuple_splitted[1]) ))


#PART 2
x_total=0
y_total=0
for coordinate in coordinates:
    x_total = x_total + coordinate[0]
    y_total = y_total + coordinate[1]

x_mean = x_total / number_of_coordinates
y_mean = y_total / number_of_coordinates

centre_of_mass = (x_mean,y_mean)
print("centre of mass is:",centre_of_mass)



#PART 3
distance = []
for coord_index in range(0,number_of_coordinates):
    first_term = (coordinates[coord_index][0] - x_mean)**2
    second_term = (coordinates[coord_index][1] - y_mean)**2
    distance.append( math.sqrt(first_term + second_term) )


#PART 4
closest_distance = min(distance)
closest_coordinate = coordinates[distance.index(min(distance))]

farthest_distance = max(distance)
farthest_coordinate = coordinates[distance.index(max(distance))]

print("closest coordinate:",closest_coordinate,"with closest distance:",closest_distance)
print("farthest coordinate:",farthest_coordinate,"with farthest distance:",farthest_distance)