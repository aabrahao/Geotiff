import System as sys
import Geotiff as gt
import numpy as np
import Cad as cad
import matplotlib.pyplot as plt
import Print as prt

def toMeter(ft):
    return ft/3.28084

def toFoot(m):
    return m*3.28084

def main():

    cell = gt.Dataset('data/rifle/terrain-masked.tif')

    cell.info()

    ax = cad.plots()
    cell.show(ax)

    # Data
    z = cell.data()

    # Indexes
    n, m = z.shape
    xi, yi = cell.toWorld(0,0)
    xn, yn = cell.toWorld(n,m)
    cad.point(ax, xi, yi, color='red')
    cad.point(ax, xn, yn, color='red')
    cad.line(ax, xi, yi, xn, yn, color='red')

    # World
    w, h = cell.width()
    x, y = cell.origin()
    cad.point(ax, x, y, color='blue')
    cad.point(ax, x + w, y + h, color='blue')
    cad.line(ax, x, y, x + w, y + h, color='blue')
        
    ax.set_xlim(x, x + w)
    ax.set_ylim(y, y + h)

    # Robot
    xr = x + 0.25*w
    yr = y + 0.25*h
    
    # Scan
    ws = toMeter(18)
    hs = toMeter(30)
    xs = xr + toMeter(1.4)
    ys = yr - hs/2
    cad.point(ax, xr, yr, color='orange')
    cad.rectangle(ax, xs, ys, ws, hs, color='orange')

    cad.title(ax, cell.name)
    cad.pause()
    
if __name__ == "__main__":
    main() 
