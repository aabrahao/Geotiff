import System as sys
import Geotiff as gt
import numpy as np
import Draw as drw
import matplotlib.pyplot as plt
import Print as prt

def toMeter(ft):
    return ft/3.28084

def toFoot(m):
    return m*3.28084

def main():

    cell = gt.Region('data/rifle/terrain-masked.tif')

    cell.info()

    fig, ax = plt.subplots(figsize=(30,28))
    cell.show(axes=ax)

    # Indexes
    n, m = cell.size()
    xi, yi = cell.world(0,0)
    xn, yn = cell.world(n,m)
    drw.circle(ax, xi, yi, 10, color='red')
    drw.circle(ax, xn, yn, 10, color='red')
    drw.line(ax, xi, yi, xn, yn, color='red')

    # World
    w, h = cell.width()
    x, y = cell.origin()
    drw.circle(ax, x, y, 10, color='blue')
    drw.circle(ax, x + w, y + h, 10, color='blue')
    drw.line(ax, x, y, x + w, y + h, color='blue')
        
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
    drw.circle(ax, xr, yr, 1, color='orange')
    drw.rectangle(ax, xs, ys, ws, hs, color='orange')

    ax.set_title(cell.filename)
    plt.show()
    
if __name__ == "__main__":
    main() 
