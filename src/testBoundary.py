import System as sys
import Geotiff as gt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import Print as prt

import Cad as cad

def show(data, ax):
    data.info()
    data.show(ax)
    x,y = data.boundary()
    if x.size != 0 and y.size != 0:
        cad.lines(ax, x, y, color='red', thickness=4)
    cad.title(ax, data.name)

def main():
    data1 = gt.Dataset('data/rifle/satellite.tif')
    data2 = gt.Dataset('data/rifle/satellite-masked.tif')
    data3 = gt.Dataset('data/rifle/terrain.tif')
    data4 = gt.Dataset('data/rifle/terrain-masked.tif')

    ((ax1, ax2), (ax3, ax4)) = cad.plots(2,2)
    show(data1, ax1)
    show(data2, ax2)
    show(data3, ax3)
    show(data4, ax4)
    cad.pause()
    
if __name__ == "__main__":
    main() 

