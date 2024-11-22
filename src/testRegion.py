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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30,28))
    
    # Cell
    cell = gt.Region('data/rifle/terrain-masked.tif')
    cell.info()
    cell.show(axes=ax1)
    ax1.set_title(cell.filename)
    
    # World
    xw, yw = cell.origin()
    ww, hw = cell.width()
    ax1.set_xlim(xw, xw + ww)
    ax1.set_ylim(yw, yw + hw)

    # Robot
    xr = xw + 0.25*ww
    yr = yw + 0.25*hw
    
    # Scan
    ws = toMeter(18)
    hs = toMeter(30)
    xs = xr + toMeter(1.4)
    ys = yr - hs/2
    drw.circle(ax1, xr, yr, 1, color='red')
    drw.rectangle(ax1, xs, ys, ws, hs, color='red')

    area = gt.Region('data/rifle/terrain-masked.tif', xw, yw, ww, hw)
    area.info()

    z = area.data()
    ax2.imshow(z)
    print(z)

    #area.show(axes=ax2)

    plt.show()
    
if __name__ == "__main__":
    main() 
