import System as sys
import Geotiff as gt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import Print as prt
import Geometry as gmt

def show(data, ax):
    data.info()
    data.show(axes=ax)
    x,y = data.boundary()
    if x.size != 0 and y.size != 0:
        ax.plot(x,y, color='red', linewidth = 4)
        for d in np.linspace(-100, 100, 4):
            xo, yo = gmt.offset(x,y, d)
            ax.plot(xo,yo, color='blue', linewidth = 4)
    ax.set_title(data.filename)

def main():
    data1 = gt.Region('data/rifle/satellite.tif')
    data2 = gt.Region('data/rifle/satellite-masked.tif')
    data3 = gt.Region('data/rifle/terrain.tif')
    data4 = gt.Region('data/rifle/terrain-masked.tif')

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(30,28))
    show(data1, ax1)
    show(data2, ax2)
    show(data3, ax3)
    show(data4, ax4)
    plt.show(block=False)

    sys.pause()
    
if __name__ == "__main__":
    main() 

