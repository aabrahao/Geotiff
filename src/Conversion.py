import numpy as np
from shapely.geometry import Polygon

###########################################
# Numpy and list

def toList(x):
    return list(x)

def fromList(l = None):
    if l is None:
        return np.empty()
    return np.array(l)

############################################
# List of points

def toPoints(x,y):
    points = list(zip(x,y))
    return points

def fromPoints(points):
    xy = np.array(points)
    return xy[:,0], xy[:,1]

############################################
# Polygons

def toPolygon(x,y):
    return Polygon(toPoints(x,y))

def fromPolygon(polygon):
    return fromPoints( list(polygon.exterior.coords) )
