import System as sys
import Geotiff as gt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import Print as prt
import Cad as cad

def main():
    data1 = gt.Dataset('data/rifle/satellite.tif')
    data2 = gt.Dataset('data/rifle/satellite-masked.tif')
    data3 = gt.Dataset('data/rifle/terrain.tif')
    data4 = gt.Dataset('data/rifle/terrain-masked.tif')

    ((ax1, ax2), (ax3, ax4)) = cad.plots(2,2)
    data1.show(ax1); cad.title(ax1, data1.name)
    data2.show(ax2); cad.title(ax2, data2.name)
    data3.show(ax3); cad.title(ax3, data3.name)
    data4.show(ax4); cad.title(ax4, data4.name)
    cad.pause()
    
if __name__ == "__main__":
    main() 
