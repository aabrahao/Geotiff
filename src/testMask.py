import System as sys
import Geotiff as gt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import Print as prt

def show(data, ax):
    data.info()
    mask = data.mask()
    ax.imshow(mask)
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
