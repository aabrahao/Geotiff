import Default as st
import Conversion as cnv

import numpy as np

from shapely.geometry import Polygon
from shapely.affinity import scale

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

def gradient(x,y,z):
    dx = x[0,1] - x[0,0]
    dy = y[1,0] - y[0,0]
    print('d:', dx, dy)
    gx, gy = np.gradient(z, dx, dy)
    return gx, gy 

def offset(x,y,distance):
    polygon = cnv.toPolygon(x,y)
    offset_polygon = polygon.buffer(distance)
    xo, yo = cnv.fromPolygon(offset_polygon)
    return xo, yo


