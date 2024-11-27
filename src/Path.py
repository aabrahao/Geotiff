import numpy as np
import matplotlib.pyplot as plt

import System as sys
import Geotiff as gt
import Print as prt
import Cad as cad
import Geometry as gmt
import Vector as vc

from math import ceil

def generateScangrid(xp, yp, d, angle = 0, ax = None):
    ox,oy,w,h = gmt.bounds(xp, yp)
    # Directions
    ux,uy = vc.direction(angle)
    nx,ny = vc.normal(ux, uy)
    # Unitary
    ux,uy = vc.unit(ux,uy)
    nx,ny = vc.unit(nx,ny)
    # Projections
    upx,upy = vc.project(ox+w,oy,ux,uy,xp,yp)
    # Ranges
    x1,y1,x2,y2 = gmt.extents(upx,upy)
    # Grid edges
    xl,yl = vc.vector()
    xr,yr = vc.vector()
    while True:
        x1,y1 = x1 + d * nx, y1 + d * ny
        x2,y2 = x2 + d * nx, y2 + d * ny
        xi,yi = gmt.intersect(xp, yp, x1, y1, x2, y2)
        if xi.size < 2 or yi.size <2:
            print('Ops, boundary open; skip grid!')
            break
        else:
            if xi.size > 2 or yi.size > 2:
                print('Ops, boundary intersec geofence multipletimes; innerpoints ignored!')
            xl,yl = vc.append(xl, yl, xi[0], yi[0])
            xr,yr = vc.append(xr, yr, xi[-1], yi[-1])
            if ax is not None:
                cad.line(ax, xl[-1], yl[-1], xr[-1], yr[-1], color = 'magenta')
                cad.point(ax, xl[-1], yl[-1], color = 'red')
                cad.point(ax, xr[-1], yr[-1], color = 'blue')
    # Zigzag
    n = vc.size(xl)
    x,y = vc.vector(2*n)
    for i, j in zip(range(0, n, 1), range(0, 2*n, 2)):
        if i % 2 == 0: # Even
            x[j]   = xr[i]; y[j]   = yr[i]
            x[j+1] = xl[i]; y[j+1] = yl[i]
        else: # Odd
            x[j]   = xl[i]; y[j]   = yl[i]
            x[j+1] = xr[i]; y[j+1] = yr[i]
    return x, y
       