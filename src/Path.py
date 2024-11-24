import numpy as np
import matplotlib.pyplot as plt

import System as sys
import Geotiff as gt
import Print as prt
import Cad as cad
import Geometry as gmt

from math import ceil

def generateScangrid(xfence, yfence, dy):
    # Grid
    xmin = min(xfence) - dy
    xmax = max(xfence) + dy
    ymin = min(yfence) + dy; 
    ymax = max(yfence)
    # Left and right fence ingtersections
    n = ceil((ymax - ymin)/dy)
    xl = np.empty(n); yl = np.empty(n)
    xr = np.empty(n); yr = np.empty(n)
    y = ymin
    for i in range(0, n):
        xi, yi = gmt.intersect(xfence, yfence, xmin, y, xmax, y)
        if xi.size < 2 or yi.size <2:
            print('Ops, boundary open; skip grid!')
        else:
            if xi.size > 2 or yi.size > 2:
                print('Ops, boundary intersec geofence multipletimes; innerpoints ignored!')
            xl[i]= xi[ 0]; yl[i] = yi[ 0]
            xr[i]= xi[-1]; yr[i] = yi[-1]
        y = y + dy
    # Zigzag path
    x = np.empty(2*n)
    y = np.empty(2*n)
    for i, j in zip(range(0, n, 1), range(0, 2*n, 2)):
        if i % 2 == 0: # Even
            x[j]   = xr[i]; y[j]   = yr[i]
            x[j+1] = xl[i]; y[j+1] = yl[i]
        else: # Odd
            x[j]   = xl[i]; y[j]   = yl[i]
            x[j+1] = xr[i]; y[j+1] = yr[i]
    return x, y
