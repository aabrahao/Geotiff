import Settings as st

import numpy as np

from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
from shapely import get_coordinates

###########################################
# Conversions

def toList(x):
    return list(x)

def fromList(l):
    return np.array(l)

def toPoints(x,y):
    points = list(zip(x,y))
    return points

def fromPoints(points):
    xy = np.array(points)
    return xy[:,0], xy[:,1]

def toLine(x,y):
    return LineString(toPoints(x,y))

def fromLine(line):
    pass

def toPolygon(x,y):
    return Polygon(toPoints(x,y))

def fromPolygon(polygon):
    return fromPoints( list(polygon.exterior.coords) )

def fromShapely(shape):
    xy = get_coordinates(shape)
    return xy[:,0], xy[:,1]

def array(n=None):
    return np.empty(n)

###########################################
# Math

def range(x):
    xmin = np.nanmin(x)
    xmax = np.nanmax(x)
    return xmin, xmax

def normalize(i1, i2):
    return min(i1, i2), max(i1, i2)

def clamp(vmin, v, vmax):
    v = max(vmin, v)
    v = min(v, vmax)
    return v

###########################################
# Numerics

def gradient(x, y, z):
    dx = x[0,1] - x[0,0]
    dy = y[1,0] - y[0,0]
    print('d:', dx, dy)
    gx, gy = np.gradient(z, dx, dy)
    return gx, gy 

###########################################
# Polygon: xp, yp

def offset(xp, yp, distance):
    polygon = toPolygon(xp, yp)
    buffer = polygon.buffer(distance)
    return fromShapely(buffer)

def contains(xp, yp, x, y):
    polygon = toPolygon(xp, yp)
    return polygon.contains(Point(x,y))

def extents(xp, yp):
    xmin = np.nanmin(xp)
    ymin = np.nanmin(yp)
    xmax = np.nanmax(xp)
    ymax = np.nanmax(yp)
    return  xmin, ymin, xmax, ymax

def bounds(xp, yp):
    xmin, ymin, xmax, ymax = extents(xp, yp)
    return  xmin, ymin, xmax-xmin, ymax-ymin

def intersect(xp, yp, x1, y1, x2, y2):
    polygon = toPolygon(xp, yp)
    line = LineString( [(x1, y1), (x2, y2)])
    lines = line.intersection(polygon)
    return fromShapely(lines)
