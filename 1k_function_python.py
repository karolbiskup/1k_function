# How to check how many functions defined in file
# ^\s*def
# Check box Use Regular Expression - tick

# Group Function
# distance (20), one side function, integer (5), area (36), 

import math


'''
Give this function length side of your square
This function return you area of square
'''
def area_square(side):

    area = side * side
    return area


'''
Give this function length sides of your rectangle
This function return you area of recangle
If you have rectangle where width is 5 and height is 10 you may call this function on 2 way:
area_rectangle(5, 10)
area_rectangle(10, 5)
'''
def area_rectangle(a, b):
    
    area = a * b
    return area

'''
Give this function radius of circle
This function return you area of circle
'''
def area_circle(r):

    area = 3.14 * r * r
    return area


'''
Give this function length base of triangle and length height of triangle
a - base of triangle
h - height of triangle
This function return you area of triangle
'''
def area_triangle(a, h):

    area = (a * h) / 2
    return area



'''
Give this function lenght of base parallelogram, and length of height parallelogram
This function return you area of parallelogram
'''
def area_parallelogram(a, h):

    area = a * h
    return area


'''
Give this function lenghs of two parallel base and lenght of height across
This function return you area of trapeze 
a - one of base
b - another of base 
h - height
If your trapeze have dimension like: 12 - base, 2 - base, 4 - height, you may call this function 
on two way:
area_trapeze(12, 2, 4)
area_trapeze(2, 12, 4)
'''
def area_trapeze(a, b, h):

    area = (a + b) * h / 2
    return area


'''
Give this function lenghts of diagonal
This function return you area of deltoid
'''
def area_deltoid(d1, d2):

    area = d1 * d2 / 2 
    return area


'''
Give this function length of side of your regular hexagon
This function return you area of regular hexagon
'''
def area_regular_hexagon(side):

    # Regular hexagon consist 6 - equilateral triangle
    # We calculate area one of triangle and on last myltiply by six to calculate area of hexagon
    # h = a * 3^(1 / 2) / 2   ->   height equilateral triangle
    area_of_one_triangle = side * (side * pow(3, 1/2) / 2) / 2

    return area_of_one_triangle * 6


'''
Give this function length of side and length of height slice triangle
This function return you area of seven regular corner
'''
def area_seven_regular_corner(side, height):

    # This function get 2 parametrs length of side and length of height our slice triangle
    # Polygon consist many triangle, our 7 regular corner polygon consist 7 the same triangle
    # We have base of this triangle and height so we calculate area of this triangle and the last
    # multipy rezult by seven to calculate area our seven regular corner
    area_of_one_triangle = side * height / 2

    return area_of_one_triangle * 7


'''
Give this function information how many corner do you have and give lenght of your side
This function return you area our regular corner
This function not work correctly
'''
def area_regular_corner_polygon(number_corner, side):

    '''
    At first we must calculate our height(slice triangle), if we have six-corner regular polygon
    Our slice triangle have 360/6 = 60 degrees. This triangle have the same length of 2 side.
    You must paint it to paper to understand formula under
    '''
    # Divide by 2 becouse we have been interested on triangle with 90 degrees angle
    angle = 360 / number_corner / 2 
    h = (side / 2) / math.tan(angle)

    # At first we calculate area slice triangle, and the next area our corner 
    area_polygon = (side * h / 2) * number_corner

    return area_polygon


'''
Give this function 2 vertex one is (x1, y1) second is (x2, y2)
This function return you area our square

This is very important your vertex must lie on the same side
'''
def area_square_2_dot(x1, y1, x2, y2):

    # First calculate sides our triangle with 90 degrees angle 
    a = abs(x1 - x2)
    b = abs(y1 - y2)

    # c is side our square
    c = pow((a * a + b * b), 1/2)

    return c * c

'''
Give this function 2 vertex one is (x1, y1) second is (x2, y2)
This function return you area our square

This is very important your vertex must lie on the same diagonal
'''
def area_square_2_dot_diagonal(x1, y1, x2, y2):

    # At first we calculate sides our triangle
    a = abs(x1 - x2)
    b = abs(y1 - y2)

    c = pow((a * a + b * b), (1 / 2))

    # square is deltoid
    return c*c / 2

'''
Give this function radius of your circle - r and count your circle - count_circle
This function return you area of group circle for example if area one circle is 100 and you
have two circle this function always return you 200
'''
def area_group_circle(r, count_circle):

    # Area of one circle is
    area_one_circle = 3.14 * r * r

    return area_one_circle * count_circle

'''
This function get 3 vertex
(a_l_x, a_l_y) -> this is one vertex
(a_p_x, a_p_y) -> this is second vertex
(b_d_x, b_d_y) -> this is another vertex

Our rezult is area of rectangle
'''
def area_rectangle_3_dot(a_l_x, a_l_y, a_p_x, a_p_y, b_d_x, b_d_y):

    # At first calculate length of a, at first we must calculate our side
    a_one = abs(a_l_x - a_p_x)
    a_two = abs(a_l_y - a_p_y)

    a = pow((a_one * a_one + a_two * a_two), (1/2))

    # Next calculate lenght of b, at first we must calculate our side
    b_one = abs(a_p_x - b_d_x)
    b_two = abs(a_p_y - b_d_y)

    b = pow((b_one * b_one + b_two * b_two), (1 / 2))

    return a*b


'''
This function get 2 vertex
x1, y1 -> this is one vertex
x2, y2 -> this is second vertex
This is very important that these vertex must lie on the same diagonal
'''
def area_rectangle_vertex_diagonal(x1, y1, x2, y2):

    # At first we must calculate our diagonal before we do this calculate side of triangle
    diagonal_one = abs(x1 - x2)
    diagonal_two = abs(y1 - y2)

    diagonal = pow((diagonal_one * diagonal_one + diagonal_two * diagonal_two), (1 / 2))

    # Our rectangle is deltoid
    return diagonal * diagonal / 2

'''
This function calculate area our circle, you must give center of your circle:
Sx, Sy
and point on circle:
x1, y1
'''
def area_circle_2_point(Sx, Sy, x1, y1):

    # We must find area at first calculate radius of circle
    radius_one = abs(x1 - Sx)
    radius_two = abs(y1 - Sy)

    radius = pow((radius_one * radius_one + radius_two * radius_two), (1 / 2))

    area_circle = 3.14 * radius * radius 

    return area_circle



'''
This function calculate area 10 square
Give this function lenght of your side 
This function return you area of 10 square
For example if we have square where side = 1 this function return you 10
'''
def area_10_square(side):

    area_one_square = side * side
    return area_one_square * 10


'''
This function calculate area 20 circle 
Give this function radius our circle
This function return you area of 20 circle 
For example if you call this function with radius equal one you get 3.14 * 20
'''
def area_20_circle(radius):
    
    area_circle = 3.14 * radius * radius 
    return area_circle * 20 


'''
This function calculate area cube
Give this function lenght of your edge and you get area of cube
'''
def area_cube(edge):

    area_square = edge * edge

    return area_square * 6



'''
This function get 3 arguments
- a (edge)
- b (edge)
- h (height our cuboid)
Our rezult is area our cuboid
'''
def area_cuboid(a, b, h):

    # We have some rectangle:
    # 2 rectangle a x b
    # 2 rectangle a x h
    # 2 rectangle b x h

    area_cuboid = (2 * a * b) + (2 * a * h) + (2 * b * h)

    return area_cuboid


'''
This function get 2 arguments:
r - radius of circle in base 
h - height our cylinder

Our rezult is area of cylinder
'''
def area_cylinder(r, h):
    
    # area our base 
    area_one_circle_base = math.pi * r * r

    # area our envelope
    area_envelope = (2 * math.pi * r) * h

    area_all = area_one_circle_base * 2 + area_envelope

    return area_all


'''
This function get radius our globe
Our rezult is area our globe
'''
def area_globe(radius):

    area_globe = 4 * math.pi * radius * radius

    return area_globe


'''
This function calculate area cone, area base + area envelope
r - radius of circle in base 
h - height cone
This function return area our cone
'''
def area_cone(r, h):

    # area base
    area_base = math.pi * r * r

    # before you calculate area envelpe
    l = pow(r * r + h * h, (1 / 2))
    obw_envelope_is = 2 * math.pi * r
    obw_envelope_could_be = 2 * math.pi * l

    alfa = obw_envelope_is / obw_envelope_could_be 

    area_envelope_could_be = math.pi * l * l
    area_envelope = area_envelope_could_be * alfa

    return (area_envelope + area_base)



'''
This function get 2 arguments:
r - radius of circle in base 
l - forming a cone
Our rezult is area cone
'''
def area_cone_l(r, l):

    # area base 
    area_base = math.pi * r * r 

    # before you calculate area envelope 
    obw_envelope_is = 2 * math.pi * r
    obw_envelope_could_be = 2 * math.pi * l
    alfa = obw_envelope_is / obw_envelope_could_be

    area_envelope_could_be = math.pi * l * l
    area_envelope = area_envelope_could_be * alfa

    area = area_base + area_envelope 

    return area



'''
This function get 2 arguents:
r - radius of circle in base
beta - angle with forming a cone and base

Our rezult is area of cone
'''
def area_cone_beta(r, beta):

    # area base 
    area_circle_base = math.pi * r * r

    # before you calculate area envelope
    l = r / math.cos(math.radians(beta))
    obw_envelope_is = 2 * math.pi * r
    obw_envelope_could_be = 2 * math.pi * l 
    alfa = obw_envelope_is / obw_envelope_could_be 

    area_envelope_could_be = math.pi * l * l
    area_envelope = area_envelope_could_be * alfa

    return area_envelope + area_circle_base


'''
This function get one argument obw, circumference of globe
Our rezult is area of globe
'''
def area_globe_obw(obw):

    # at first calculate r
    # 2 * pi * r = Obw
    # r = Obw / 2 * pi
    r = obw / (2 * math.pi)

    area = 4 * math.pi * r * r

    return area


'''
This function get 2 arguments:
h - height our cylinder 
obw - circumference our circle in base

Our rezult is area cylinder
'''
def area_cylinder_obw(h, obw):

    # at first calculate r 
    # 2 * pi * r = obw
    # r = obw / (2 * pi)
    r = obw / (2 * math.pi)

    # area circle in base
    area_base_circle = math.pi * r * r

    # area rectangle
    area_envelope_rectangle = obw * h 

    # area our cylinder
    area = 2 * area_base_circle + area_envelope_rectangle

    return area 


'''
This function calculate area regular quadrangular pyramid, get 2 arguments:
side - edge in base our pyramid
h - height our pyramid

Our rezult is area pyramid
'''
def area_regular_pyramid(side, h):

    # If we have regular quadrangular pyramid we have 4 the same triangle
    # at first we must find height this triangle
    height_triangle = pow((side/2) * (side/2) + h * h, (1/2))

    area_one_triangle = side * height_triangle / 2

    # area in base 
    area_base_square = side * side 

    # sum area
    area = area_base_square + area_one_triangle * 4 

    return area


'''
simple - mean that height go throught center of rectangle in base
This function get 3 arguments:
a - one of edge
b - another edge
h - height our pyramid
'''
def area_simple_pyramid_rectangle_in_base(a, b, h):

    # area rectangle in base
    area_base_rectangle = a * b

    # If we have simple pyramid we have:
    # 2 triangle where a is base -> we have height height_a_base
    # 2 triangle where b is base -> we have height height_b_base

    # at first calculate height_b_base
    height_b_base = pow((a / 2)* (a / 2) + h * h, (1 / 2))

    # calculate height_a_base
    height_a_base = pow((b / 2) * (b / 2) + h * h, (1 / 2))

    area_2_triangle_a = (a * height_a_base / 2) * 2
    area_2_triangle_b = (b * height_b_base / 2) * 2 

    # sum area
    area = area_base_rectangle + area_2_triangle_a + area_2_triangle_b

    return area 


'''
This function takes one argument
- (side) this is lengh of your edge 
This function returns the area of a tetrahedron
'''
def area_tetrahedron(side):

    # Calculate area one triangle
    area_equilateral_triangle = side * (side * 3 ** (1 / 2) / 2) / 2

    return area_equilateral_triangle * 4



'''
This function takes one argument
obw - this is sum of your all side in square
This function returns the area of your square
'''
def area_square_obw(obw):

    # at first calculate side of your square
    a = obw / 4

    #  next calculate area of your square
    area = a ** 2

    return area



"""
This function takes 2 arguments 
perim - this is sum all sides of your rectangle
side - this is one of your side (doesn't important witch)
This functon returns the area of your rectangle
"""
def area_rectangle_perim(perim, side):

    # at first calculate sum of 2 another side (or the same if we have square, square is rectangle)
    sum_two_another_side = perim / 2 

    # next calculate sides (a, b), we have sum a + b and one of side - side
    a = sum_two_another_side - side 
    b = side

    area = a * b 

    return area


"""
This function takes one argument:
circumference - This argument is circumference of your square
This function returns area of circle
"""
def area_circle_circumference(circumference):

    # at first calculate radius of your circle 
    # (2 * pi) * r = perim
    # r = perim / (2 * pi)
    radius = circumference / (2 * math.pi)

    # calculate area of your circle
    area = math.pi * radius ** 2 

    return area



'''
This function takes 2 arguments:
alfa - the angel of our slice circle
radius - the radius of our circle
This function returns the area of your circle
'''
def area_slice_circle(alfa, radius):

    # The ratio of the slice circle to the imagine circle is:
    ratio = alfa / 360

    # Calculate area of the imagine circle
    area_imagine_circle = math.pi * radius ** 2 

    area = area_imagine_circle * ratio 

    return area


'''
This function takes three arguments
These arguments correspond to the side lengths
This function returns the area of your triangle
'''
def area_triangle_all_side(a, b, c):

    # We have 3 sides of the triangle, we use Heron's formula to calculate area of the triangle
    
    # At first, calculate semi-perimeter
    semi_perimeter = (a + b + c) / 2

    # Heron's formula
    area_triangle = pow((semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)), (1/2))

    return area_triangle


'''
This function takes three arguments:
a - one side
b - another side
angel_between - angel between a and b side (in degrees)
This function returns the area of your triangle
'''
def area_triangle_2_side_angel_between(a, b, angel_between):

    # We use Law of Cosines to calculate third side and the next use Heron's formula
    c = pow((a ** 2 + b ** 2 + 2 * a * b * math.cos(math.radians(angel_between))), (1 / 2))

    # At first, calculate semi-perimeter 
    semi_perimeter = (a + b + c) / 2

    # Heron's formula
    area_triangle = pow((semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter -c)), (1 / 2))

    return area_triangle


'''
Imagine that your specifically defined function y = 1/2 * x^2 + 3 is one side 
and the other side is x axis on range a to b (reverse arguments give the same rezult)
This function returns area of this shape
'''
def one_side_function_another_side_x_axis(a, b):

    # After integrating function y = 1/2 * x^2 + 3 we obtain 1/6 * x^3 + 3*x + C

    # At first find smallest and bigger integer
    if a>b:
        bigger_integer = a
        smallest_integer = b
    else:
        bigger_integer = b
        smallest_integer = a

    # Substitute at first bigger integer to formula 1/6 * x^3 + 3*x
    VALUE_ON_BIGGER = (1/6) * pow(bigger_integer, 3) + 3 * bigger_integer

    # Substitute smallest integer to formula 1/6 * x^3 + 3*x
    VALUE_ON_SMALLEST = (1/6) * pow(smallest_integer, 3) + 3 * smallest_integer

    return VALUE_ON_BIGGER - VALUE_ON_SMALLEST


'''
Imagine that your specifically defined function y = x is one side and the other side is 
x axis in range a to b (reverse arguments give the same rezult)
This function returns area of this shape (if area above x axis we take this area on plus,
if area under axis x we take this area on minus and built our rezult)
'''
def one_side_function_x_another_side_x_axis(a, b):

    # At first find smallest and bigger integer
    if a>b:
        bigger_integer = a 
        smallest_integer = b
    else:
        bigger_integer = b
        smallest_integer = a 

    # After integrating function y = x we obtain y = (1/2) * x^2

    # Substitute at first bigger integer to formula y = (1/2) * x^2
    VALUE_ON_BIGGER = (1/2) * pow(bigger_integer, 2) 

    # Substitute smallest integer to formula y = (1/2) * x^2
    VALUE_ON_SMALLEST = (1/2) * pow(smallest_integer, 2)    

    return VALUE_ON_BIGGER - VALUE_ON_SMALLEST




'''
Imagine that your specifically defined function y = x is one side and the other side is
x axis in range a to b (imagine this shape). Prior we built our rezult that area above x-axis
is taken on plus, but area under x-axis is taken on minus. In this case area above x-axis is 
taken on plus, but area under x-axis is taken either plus. 

If we reverse arguments (range) we get the same rezult

This function returns area of this shape
'''
def one_side_function_x_another_side_x_axis_up(a, b):

    # After integrating function y = x we obtain y = (1/2) * x^2

    # At first choose bigger and smallest integer from integer a and b 
    if a>b:
        bigger_integer = a 
        smallest_integer = b 
    else:
        bigger_integer = b
        smallest_integer = a


    
    VALUE_ON_BIGGER = (1/2) * bigger_integer ** 2
    VALUE_ON_SMALLEST = (1/2) * smallest_integer ** 2

    if (smallest_integer < 0) and (bigger_integer > 0):
        return VALUE_ON_BIGGER + VALUE_ON_SMALLEST
    else:
        return abs(VALUE_ON_BIGGER - VALUE_ON_SMALLEST)
    

'''
Imagine that your specifically defined function y = 2x^2 + 6 is one side and the other side is
x-axis in range a to b (imagine this shape). This function is allways above x axis. 

If we reverse arguments (range) we get the same rezult

This function returns the area of this shape
'''
def one_side_function_another_side_x_axis_1(a, b):

    # After integrating function y = 2x^2 + 6 we obtain y = (2/3)*x^3 + 6x

    # At first choose bigger and smallest integer on integer a and integer b
    if a>b:
        bigger_integer = a
        smallest_integer = b
    else:
        bigger_integer = b
        smallest_integer = a 
    
    # Substitute smallest integer to formula y = (2/3)*x^3 + 6x
    VALUE_ON_SMALLEST = (2/3) * smallest_integer ** 3 + 6 * smallest_integer 

    # Substitute bigger integer to formula y = (2/3)*x^3 + 6x
    VALUE_ON_BIGGER = (2/3) * bigger_integer ** 3 + 6 * bigger_integer 

    return VALUE_ON_BIGGER - VALUE_ON_SMALLEST 


'''
Imagine that your specifically defined function y = x^3 is one side and the other side is
x-axis in range a to b (imagine this shape). If area is under x-axis we take this area on plus,
if area is above x-axis we take this area on plus and build rezult

If we reverse arguments (range) we get the same rezult

This function returns the area of this shape
'''
def one_side_function_another_side_x_axis_2(a, b):

    # After integrating function y = x^3 we obtain y = (1/4) * x^4
    
    # At first choose bigger and smallest integer from integer a and integer b
    if a>b:
        bigger_integer = a 
        smallest_integer = b
    else:
        bigger_integer = b
        smallest_integer = a 

    # Substitute smallest integer to formula y = (1/4) * x^4
    VALUE_ON_SMALLEST = (1/4) * smallest_integer ** 4
    
    # Substitute bigger integer to formula y = (1/4) * x^4
    VALUE_ON_BIGGER = (1/4) * bigger_integer ** 4



    if (smallest_integer<0) and (bigger_integer>0):
        return VALUE_ON_BIGGER + VALUE_ON_SMALLEST
    else:
        return abs(VALUE_ON_BIGGER - VALUE_ON_SMALLEST)


# Distance

'''
This function takes two arguments: 
x - x-coordinate of point
y - y-coordinate of point
This function returns the distance on origin
'''
def distance_point_to_origin(x, y):

    distance = (x ** 2 + y ** 2) ** 0.5
    return distance


'''
This function takes four arguments:
(x, y) - one point
(x1, y1) - second point
This function returns the distance between 2 points
'''
def distance_two_point(x, y, x1, y1):

    diff_x = abs(x - x1)
    diff_y = abs(y - y1)
    distance = (diff_x ** 2 + diff_y ** 2) ** 0.5

    return distance



'''
This function returns the distance (in m) between Earth and Moon
This function has no parameters
'''
def distance_Moon_Earth():
    
    distance_km = 384400
    distance_m = distance_km * 1000

    return distance_m


'''
This function show the distance (in m) between Earth and Moon
This function has no parameters
Dispays a message in the terminal. No return value
'''
def distance_Moon_Earth_show():

    distance_km = 384400
    print(f"Distance between Earth and Moon is: {distance_km * 1000} m")



'''
This function show the distance (in cm) between Earth and Moon
This function has no parameters
Displays a message in the terminal. No return value
'''
def distance_Moon_Earth_cm_show():

    distance_km = 384400
    distance_m = distance_km * 1000 
    distance_cm = distance_m * 100

    print(f"Distance between Earth and Moon is: {distance_cm} cm")


'''
This function show the distance (in mm) between Earth and Moon
This function has no parameters
Displays a message in the terminal. No return value
'''
def distance_Moon_Earth_mm_show():
    distance_km = 384400
    distance_m = distance_km * 1000
    distance_cm = distance_m * 100
    distance_mm = distance_cm * 10

    print(f"Distance between Earth and Moon is: {distance_mm} mm")


'''
This function show the distance (in km) between Earth and Moon
This function has no parameters
Displays a message in the terminal. No return value
'''
def distance_Moon_Earth_km_show():
    distance_km = 384400

    print(f"Distance between Earth and Moon is: {distance_km} km")



'''
This function show the distance (in m) between Mercury and Earth (average)
This function has no parameters
Displays a message in the terminal. No return value
'''
def distance_Mercury_Earth_show():
    distance_million_km = 155
    distance_km = distance_million_km * 10 ** 6
    distance_m = distance_km * 1000

    print(f"Distance between Mercury and Earth is: {distance_m} m")


'''
This function show the distance (in m) between Venus and Earth (average)
This function has no parameters
Displays a message in the terminal. No return value
'''
def distance_Venus_Earth_show():
    distance_million_km = 170
    distance_km = distance_million_km * 10 ** 6
    distance_m = distance_km * 1000

    print(f"Distance between Venus and Earth is: {distance_m} m")


'''
This function show the distance (in m) between Jupiter and Earth (average)
This function has no parameters 
Displays a message in the terminal. No return value
'''
def distance_Jupiter_Earth_show():
    distance_million_km = 778
    distance_km = distance_million_km * 10 ** 6
    distance_m = distance_km * 1000

    print(f"Distance between Jupiter and Earth is: {distance_m} m")



'''
This function show the distance (in m) between Saturn and Earth (average)
This function has no parameters
Displays a message in the terminal. No return value
'''
def distance_Saturn_Earth_show():
    distance_billion_km = 1.43
    distance_km = distance_billion_km * 10 ** 9
    distance_m = distance_km * 1000

    print(f"Distance between Saturn and Earth is: {distance_m} m")



'''
This function takes 6 arguments:
(x1, y1) - Point A 
(x2, y2) - Point B
(x3, y3) - Point C

We have 3 distance:
A - B 
A - C
B - C

This function returns the maximum distance
'''
def max_distance_3_point(x1, y1, x2, y2, x3, y3):

    # We have 3 point, so we have 3 distance

    distance_1 = 0
    distance_2 = 0
    distance_3 = 0

    # Calculate distance_1
    # (x1, y1) - (x2, y2)
    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)

    distance_1 = (diff_x ** 2 + diff_y ** 2) ** 0.5

    # Calculate distance_2
    # (x1, y1) - (x3, y3)
    diff_x = abs(x1 - x3)
    diff_y = abs(y1 - y3)

    distance_2 = (diff_x ** 2 + diff_y ** 2) ** 0.5

    # Calculate distance_3
    # (x2, y2) - (x3, y3)
    diff_x = abs(x2 - x3)
    diff_y = abs(y2 - y3)

    distance_3 = (diff_x ** 2 + diff_y ** 2) ** 0.5

    maximum_distance = max(distance_1, distance_2, distance_3)

    # Return the maximum distance
    return maximum_distance


'''
This function takes 2 arguments:
width - width your matrix
height - height your matrix
This function returns the diagonal of your matrix
'''
def diagonal_matrix(width, height):

    # Apply the Pythagorean Theorem to calclulate the distance
    diagonal = (width ** 2 + height ** 2) ** 0.5

    return diagonal


'''
This function change height to temperature
This function takes one argument:
height - height on the thermometr (in cm)
This function returns the temperature, remember on standard
'''
def change_height_temp(height):

    # Our standard is 1 cm - 5 degrees Celcius

    temp = height * 5 
    return temp


'''
This function calculate distance, when we know speed and time
This function takes two arguments:
speed 
time
This function returns the distance
'''
def calculate_distance(speed, time):
    
    # v = s/t
    # v * t = s

    # Apply the formula s = v * t
    distance = speed * time

    return distance


'''
This function calculate speed, when we know distance and time
This function takes 2 arguments:
distance
time
This function returns the speed
'''
def calculate_speed(distance, time):

    # v = s/t
    speed = distance / time

    return speed



'''
This function calculate time, when we know speed and distance
This function takes two argumetns:
speed
distance
This function returns the time
'''
def calculate_time(speed, distance):

    # v = s / t
    # v * t = s
    # t = s / v

    time = distance / speed

    return time


'''
This function change meters to kilometers
This function takes one argument:
count_meters
This function returns count kilometers
'''
def change_meters_kilometers(count_meters):

    return count_meters / 1000


'''
This function change meters to centimeters
This function takes one argument:
count_meters
This function returns count centimeters
'''
def change_meters_centimeters(count_meters):

    return count_meters * 100



'''
This function change meters to millimeters
This function takes one argument:
count_meters
This function returns count millimeters
'''
def change_meters_millimeters(count_meters):

    return count_meters * 100 * 10


# arithmetic sequence

# Show some first term 
"""
# 1 
This function show 5 first term of the sequence
We know formula of this sequence, is: an = 2n + 1
We not give function argument and function nothing return
"""
def show_5_term_sequence_is_know():

    for i in range(1, 6):
        print(f"The {i} term of our sequence is: {2 * i + 1}")

"""
# 2
This function show 5 first term of the sequence
We must give function 2 arguments: A, B
Those arguments speciffy sequence, an = An + B
Function nothing return
"""
def show_5_term_sequence_parametrs(A, B):

    for i in range(1, 6):
        print(f"The {i} term of our sequence is: {A * i + B}, sequence is an = {A}n + {B}")


"""
# 3
This function show C first term of our sequence
Function takes 3 parametrs: A, B, C
Parametrs: A, B speciffy our sequence, an = An + B
Function nothing return
"""
def show_C_term_sequence_parametrs(A, B, C):

    for i in range(1, C+1):
        print(f"The {i} term of our sequence is: {A * i + B}, sequence is an = {A}n + {B}")


# Show term under properlly index
"""
# 4
This function show term under properlly index
Function takes one argument:
index - this is index our term who must be printed on screen 

Our sequence is speciffy it is, an = 2n + 1
Function nothing return
"""
def show_term_under_index_sequence_is_know(index):

    print(f"The {index} term in sequence is: {2*index + 1}")


"""
# 5
This function show term under properlly index
Function takes 3 arguments: A, B, index
A, B - Speciffy formula our sequence, an = An + B
index - Speciffy term 

This function nothing return
"""
def show_term_under_index_sequence_parametrs(A, B, index):

    print(f"The {index} term in sequence an = {A}n + {B} is: {A * index + B}")


# Show terms from start to stop
"""
# 6
This function show some term in sequence from index_start to index_stop (inclusive)
Function takes 2 arguments: index_start, index_stop


Our sequence is speciffy is: an = 2n + 1
This function nothing return
"""
def show_some_term_sequence_is_know(index_start, index_stop):

    for i in range(index_start, index_stop + 1):
        print(f"The term where index = {i} is: {2 * i + 1}")


"""
# 7
This function print some term from index_start to index_stop (inclusive) on our sequence
Function takes 4 arguments:
index_start, index_stop
A, B - Those parametrs speciffy our sequence, an = An + B
Function nothing return
"""
def show_some_term_sequence_parametrs(index_start, index_stop, A, B):

    for i in range(index_start, index_stop + 1):
        print(f"The term where index = {i} is: {A * i + B}, sequence is: an = {A}n + {B}")


# Minimum in our sequence
"""
# 8
This function return minimum value on our sequence
Function takes 2 arguments: A, B

Those arguments speciffy sequence, an = An + B
Function return minimum value in our sequence or text NO MINIMUM
"""
def find_minimum_sequence_parametrs(A, B):

    # Check parametr A if those parametr is greather than 0 this mean that our sequence 
    # have minimum becouse this sequence on greather argument have greather value
    if A > 0:
        return ( A * 1 + B )
    
    elif A == 0:
        return B 
    
    # In this situation our sequence on greather argument have smaller value
    # so we not may find the smallest value, return text
    elif A < 0:
        return "NO MINIMUM"
        

"""
# 9
This function return index witch corresponding term who have the smallest value
Function takes 2 arguments: A, B

Those arguments speciffy sequence, an = An + B
Function return index or text:
ALL TERM HAVE THE SAME VALUE, ALL INDEX
THIS SEQUENCE NO HAVE MINIMUM
"""
def seq_index_corresponding_minimum(A, B):

    # If A is greather than 0 this mean that minimum value exist in first term, so index equal 1
    if A > 0:
        
        return 1
    
    elif A == 0:

        return "ALL TERM HAVE THE SAME VALUE, ALL INDEX"
    
    else:

        return "THIS SEQUENCE NO HAVE MINIMUM"
    


"""
# 10
This function return minimum value from begin to end our sequence
Function takes 4 arguments: 
A, B -> Speciffy our sequence, an = An + B
begin, end -> We search minimum from begin to end

Function return minimum value or text:
ALL TERM FROM INDEX {begin} TO INDEX {end} HAVE THE SAME VALUE, INDEX -> [{begin}, {end}]
"""
def find_minimum_sequence_from_to(A, B, begin, end):

    # Check A, if A is greather than 0 this mean that on 
    # greather argument we have greather value
    if A > 0: 

        return (A * begin + B)
    
    elif A == 0:

        return f"ALL TERM FROM INDEX {begin} TO INDEX {end} HAVE THE SAME VALUE, INDEX -> [{begin}, {end}]"
    
    else: 

        return (A * end + B)
    

"""
# 11
This function return index corresponding with term who have minimum value
Those function takes 4 arguments:
A, B - Speciffy our sequence, an = An + B
begin, end - Speciffy where we search our index 

Function return index or text:
ALL TERM FROM INEDX {begin} TO INDEX {end} HAVE THE SAME VALUE, INDEX -> [{begin}, {end}]"
"""
def seq_index_corresponding_min_from_to(A, B, begin, end):

    # Chceck A, if A is greather than 0 this mean
    # that on greather argument we have greather value
    if A > 0:
        
        return begin
    
    elif A == 0:

        return f"ALL TERM FROM INEDX {begin} TO INDEX {end} HAVE THE SAME VALUE, INDEX -> [{begin}, {end}]"
    
    else:

        return end
    

# Maximum in our sequence
"""
# 12
This function return max value on our sequence
Function takes 2 arguments:
A, B - Speciffy our sequence, an = An + B

Those function return maximum value or text: 
THIS SEQUENCE HAVE HIGHER VALUE
ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}
"""
def find_maximum_sequence_parametrs(A, B):

    # Check A, if A is greather than 0 this mean
    # that on greather argument we have greather value
    if A > 0:

        return f"THIS SEQUENCE HAVE HIGHER VALUE"
    
    elif A == 0:

        return f"ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}"
    
    # In this situation, max value exist on first term
    else: 

        return A * 1 + B 
    

"""
# 13
This function return index corresponding maximum value (sequence)
Function takes 2 arguments: 

A, B - Speciffy our sequence, an = An + B
Those function return index or text:
THIS SEQUENCE HAVE GREATHER VALUE
ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}
"""
def seq_index_corresponding_maximum_value(A, B):

    # Check A, if A is greather than 0 this mean
    # that on greather argument we have greather value

    if A > 0:
        
        return "THIS SEQUENCE HAVE GREATHER VALUE"
    
    elif A == 0:

        return f"ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}"
    
    # In this situation max value exist in first term, so we must return 1
    else: 

        return 1

"""
# 14
This function return maximum value on begin to end (sequence)
Function takes 4 arguments:

A, B - Speciffy our sequence, an = An + B
begin, end - Speciffy where we search our maximum value from index begin to index end
Those function return maximum value or text:
ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}
"""
def find_maximum_sequence_from_to(A, B, begin, end):

    # Check A, if A is greather than 0 this mean
    # that on greather argument we have greather value
    if A > 0:
        
        return A * end + B
    
    elif A == 0:

        return f"ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}"
    
    # In this situation, max value exist in termfirst 
    elif A < 0:

        return A * begin + B


"""
# 15
This function return index corresponding maximum value (sequence)
Function takes 4 arguments:

A, B - Speciffy our sequence, an = An + B
begin, end - Speciffy where we search our index, from begin to end
This function return index or text:
ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}
"""
def seq_index_corresponding_max_from_to(A, B, begin, end):

    # Check A, if A is greather than 0 this mean 
    # that on greather argument we have greather value
    if A > 0:

        return end
    
    elif A == 0:

        return f"ALL TERM OF THOSE SEQUENCE HAVE THE SAME VALUE: {B}"
    
    # In this situation, max value exist in first term, so we must return begin
    else:

        return begin
    
# Can we find value in sequence?
"""
# 16
This function check that value exist or no in our sequence, sequence have formula:
an = 2n + 6 ( is defined! )

This function takes one argument: value
Function return one of those text:
NO THIS VALUE NOT EXIST
YES THIS VALUE EXIST IN OUR SEQUENCE, value: {value} for index: {(value - 6) / 2
"""
def check_value_exist_in_sequence(value):
 
    # Formula our sequence is:
    # an = 2n + 6

    # (an - 6) / 2 = n

    if (value - 6) % 2:

        # This mean that exist argument witch give properlly value, but this argument
        # is not integer
        return "NO THIS VALUE NOT EXIST"
    
    else:

        return f"YES THIS VALUE EXIST IN OUR SEQUENCE, value: {value} for index: {(value - 6) / 2}"


"""
# 17
This function check that digit 3 exist or no in our sequence
Function takes 2 arguments:
A, B - Those arguments define our sequence, an = An + B
Function return text:
YES, EXIST
or
NO, NOT EXIST
"""
def check_3_exist_in_sequence(A, B):

    # If our sequence is constant
    if A == 0:

        # All term have value equal B
        if B == 3:

            return "YES, EXIST"
        
        else:

            return "NO, NOT EXIST"
    
    else:


        # NO, NOT EXIST -> show when we have rest or when n < 1
        # In this place A != 0

        if ( (3 - B) % A ) or ( ((3 - B) // A) < 1 ):

            # Exist some argument who give value 3, but this argument is not integer
            # or maybe integer but less than 1
            return "NO, NOT EXIST"
        
        else:

            return "YES, EXIST"


"""
# 18
This function check that value C exist or no in our sequence
Function takes 3 arguments: A, B, C
A, B - Those arguments speciffy our sequence, an = An + B
C - We want check if this value exist or no in our sequence
Function return text:
YES, EXIST
or
NO, NOT EXIST
"""
def if_number_exist_sequence(A, B, C):

    # This mean that we have constant sequence
    if A == 0:

        # All term in this sequence have value equal B
        if B == C:
            return "YES, EXIST"
        
        else:
            return "NO, NOT EXIST"
        
    else:

        # Formula of our sequence is:
        # an = An + B
        # (C - B)/A = n

        # In this place A != 0
        if ( (C - B) % A ) or ( ( (C - B)//A ) < 1 ):

            # Yes, exist argument witch give value C but this argument is not integer 
            # or mayby integer but less than 1
            return "NO, NOT EXIST"
        
        else:

            return "YES, EXIST"


# Check if our sequence is: increasing, decreasing, constant
"""
# 19
This function check that our sequence is increasing
Function takes 2 arguments:
A, B - Those arguments speciffy our sequence, an = An + B
Function return True when sequence is increasing or False when is constant or decreasing
"""
def is_increasing_sequence(A, B):

    if A > 0:
        return True
    
    else:
        return False
    

"""
# 20
This function check that our sequence is decreasing
Function takes 2 arguments:
A, B - Those arguments speciffy our sequence, an = An + B
Function return True when sequence is decreasing or False when increasing or constant
"""
def is_decreasing_sequence(A, B):

    if A < 0:

        return True
    
    else:

        return False


"""
# 21
This function check that our sequence is constant
Function takes two arguments: 

A, B - Those arguments speciffy our sequence, an = An + B
Function return True when sequence is constant or False when increasing, decreasing
"""
def is_constant_sequence(A, B):

    if A == 0:

        return True
    
    else:

        return False
    


"""
# 22
This function check that our sequence is: increasing, decreasing, constant
Function takes 2 arguments:
A, B - Those arguments speciffy our sequence, an = An + B
Function return one text on group below:
INCREASING
CONSTANT
DECREASING
"""
def check_sequence_up_down_constant(A, B):

    if A > 0:

        return "INCREASING"
    
    elif A == 0:

        return "CONSTANT"
    
    elif A < 0:

        return "DECREASING"
    



"""
# 23
This function check that 10 exist or no in our sequence
Our sequence is defined, it have formula:
an = 2n + 6
Function takes 2 arguents:
begin, end - we search value 10 start from index begin and end to index end
Function return:
YES -> when 10 exist
NO -> when 10 not exist
"""
def check_10_exist_in_sequence_from_to(begin, end):
 
    # Our sequence is defined, an = 2n + 6
    # Our sequence get value 10 for n equal 2

    if (end >= 2) and (begin <= 2):

        return "YES"
    
    else:

        return "NO"


"""
# 24
This function check that number 10 exist or no in our sequence
Function takes 4 arguments:
A, B - Those arguments speciffy our sequence, an = An + B
begin, end - We search value 10 start from index begin and stop on end index
Function return one of text below:
YES - If 10 exist in our sequence
NO - If 10 no exist in our sequence
"""
def check_10_exist_in_seq_parametrs_from_to(A, B, begin, end):

    # Formula our sequence is:
    # an = An + B
    # (an - B)/A = n

    # I think that letter in code I must "divide" by A so I here check A is equal zero
    if(A == 0):

        # All term of our sequence have value equal B
        if((B == 10) and (begin<=end)):
            
            return "YES"
        
    else:

        # Calculate index for we get value 10
        index_10 = (10 - B) / A


        if( ((10 - B) % A) or (index_10 < 1) ):
            
            return "NO"
        
        else:

            # In this place exist argument (index_10) in our sequence with give value 10
            # Look for begin and end
            if ((index_10 <= end) and (index_10 >= begin)):

                return "YES"
            
            else:

                return "NO"

"""
# 25
This function check that number C exist or no in our sequence
Function takes 4 arguments:
A, B - Those arguments speciffy our sequence, an = An + B
C - We want know, that this value exist or no in our sequence
begin, end - We search our value (C) from index begin to index end
Function return one of text below:
YES - When number exist
NO - When number not exist
"""          
def if_number_exist_in_seq_parametrs_from_to(A, B, C, begin, end):

    # Formula of our sequence is:
    # an = An + B
    # We must check that C exist or no in our sequence
    # (C - B)/A = n

    # I think that letter in code we must "divide" by A so in this place
    # we must analyze what we achive when A equal 0
    if A == 0:

        # In this case, all term of our sequence have the same value equal B
        if ((B == C) and (begin <= end)):
            return "YES"
        
        else:

            return "NO"
        
    else:

        # In this place A not equal 0

        # Say, we achive value C for what number of index
        index_C = (C - B)/A


        if( ((C - B) % A) or (index_C < 1) ):

            return "NO"
        
        else:

            # In this place, in our sequence exist argument(index_C) witch give value C
            # Look for begin and end
            if( (index_C <= end) and (index_C >= begin) ):
                
                return "YES"
            
            else:

                return "NO"
            
# Check sequence is increasing, decreasing, constant (Our term is hold in array)
# This thing is not strong connect with arithmetic sequence 
"""
# 26
This function check that our term in array is strictly increasing
Function takes array of our term 

Function return one of text below:
YES, SEQUENCE IS STRICTLY INCREASING
NO, SEQUENCE IS NOT STRICTLY INCREASING
"""
def check_term_is_strictly_increasing(term_sequence):

    # This loop compare 2 term together
    # i have value:
    # 1 -> first iteration (show on second element in array)
    # len(term_sequence) - 1 -> last iteration (show on last element in array)
    for i in range(1, len(term_sequence)):

        if(term_sequence[i] > term_sequence[i - 1]):
            
            # You still here, does something not stop function
            if i == len(term_sequence) - 1:
                return "YES, SEQUENCE IS STRICTLY INCREASING"
        
        else:

            # We must check if our sequence is strictly increasing if one compare is not
            # good this mean that our sequence is not strictly increasing
            return "NO, SEQUENCE IS NOT STRICTLY INCREASING"


"""
# 27
This function check that our term is strictly decreasing
Function takes array of our term
Function return one of text below:
YES, THIS SEQUENCE IS STRICTLY DECREASING
NO, THIS SEQUENCE IS NOT STRICTLY DECREASING
"""
def check_term_is_strictly_decreasing(term_sequence):

    # This loop compare together 2 element
    # i have value:
    # 1 -> first iteration (show on second element in array)
    # len(term_sequence) - 1 -> last iteration (show on last element in array)
    for i in range(1, len(term_sequence)):

        if(term_sequence[i] < term_sequence[i - 1]):

            # You still here, does something not stop work function
            if ( i == (len(term_sequence) - 1) ):
                return "YES, THIS SEQUENCE IS STRICTLY DECREASING"
        
        else:

            # If our compare is not good, this mean that our sequence is not 
            # strictly decreasing
            return "NO, THIS SEQUENCE IS NOT STRICTLY DECREASING"


"""
# 28
This function check that our sequence is constant
Function takes array of number
Function return one of text below:
SEQUENCE IS CONSTANT
SEQUENCE IS NOT CONSTANT
"""
def check_term_is_constant(term_sequence):

    # i have value:
    # 1 -> first iteration (show on second element in array)
    # len(term_sequence) - 1 -> last iteration (show on last element in array)
    for i in range(1, len(term_sequence)):

        if( term_sequence[i] == term_sequence[i-1] ):

            if ( i == (len(term_sequence) - 1) ):

                # You are still here, does something not stop program
                return "SEQUENCE IS CONSTANT"
            
        else:

            # If our compare is not good, this mean that our sequence is not constant
            return "SEQUENCE IS NOT CONSTANT"
        

"""
# 29
This function check trend our term
Function takes array of term
Function return one of text below:
OUR SEQUENCE IS INCREASING
OUR SEQUENCE IS DECREASING
OUR SEQUENCE IS CONSTANT
"""
def check_trend_sequence(term_sequence):

    value_increasing = 0
    value_decreasing = 0
    value_constant = 0

    # i have value:
    # 1 -> first iteration (show on second element in array)
    # len(term_sequence) - 1 -> last iteration (show on last element in array)
    for i in range(1, len(term_sequence)):

        # We use in code 2 variable: value_term, value_before_term
        value_term = term_sequence[i]
        value_before_term = term_sequence[i - 1]

        # If our sequence is constant
        if(value_term == value_before_term):
            value_constant += 1

        # If our sequence is increasing
        elif(value_term > value_before_term):
            value_increasing += 1

        # If our sequence is decreasing
        elif(value_term < value_before_term):
            value_decreasing += 1


    # At first i have value 1, i-1 have value 0
    # Allways we make len(term_sequence) - 1 compare

    # If we have this trend
    if(value_increasing == (len(term_sequence) - 1)):
        return "OUR SEQUENCE IS INCREASING"
        
    # If we have this trend
    elif(value_decreasing == (len(term_sequence) - 1)):
        return "OUR SEQUENCE IS DECREASING"
        
    # If we have this trend
    elif(value_constant == (len(term_sequence) - 1)):
        return "OUR SEQUENCE IS CONSTANT"
    
    else:
        return "NOT KNOW"
    
"""
# 30
This function check that our terms is strictly increasing from index begin to inex stop
Function takes 3 arguments:
term_array - This is array of our term
begin, end - We check that our sequence is increasing from index begin to index stop
"""
def check_term_is_strictly_increasing_from_to(term_array, begin, end):

    # i in this loop take value:
    # begin -> first iteration (show on properlly element)
    # end -> last iteration (show on properlly element)
    for i in range(begin, end+1):
        if(term_array[i] > term_array[i - 1]):

            # You are still here, does something not stop function.
            if i == end:
                return "THIS TERM IS INCREASING"
            
        else:
            
            # If we are in this place this mean that compare is not good so
            # our term is not increasing
            return "THIS TERM IS NOT INCREASING"

