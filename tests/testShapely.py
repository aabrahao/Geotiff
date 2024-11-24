from shapely import LineString, Point, MultiLineString
from shapely import get_coordinates

point = Point(0, 0)
line1 = LineString( [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4)] )
line2 = LineString( [Point(0, 0), Point(10, 10), Point(20, 20), Point(30, 30), Point(40, 40)] )
lines = MultiLineString( [line1, line2] )

print(point)
print(line1)
print(line2)
print(lines)

print( get_coordinates(point) )
print( get_coordinates(line1) )
print( get_coordinates(line2) )
print( get_coordinates(lines) )

