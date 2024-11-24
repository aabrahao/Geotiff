import numpy as np
import matplotlib.pyplot as plt

import System as sys
import Geotiff as gt
import Print as prt
import Cad as cad
import Geometry as gmt
import Path as pth


from math import ceil

def main():

    # Satellite image
    cell = gt.Dataset('data/rifle/satellite.tif')

    # Elevation
    z = gt.Dataset('data/rifle/terrain-masked.tif')
    xb,yb = z.boundary()
    xf, yf =  gmt.offset(xb, yb, -30)

    # Draw
    ax1 = cad.plots()
    cad.dataset(ax1, cell)
    cad.lines(ax1, xb, yb, 'red')
    #cad.curve(ax1, xf, yf, 'blue')
    
    x, y = pth.generateScangrid(xf, yf, 25)
    
    cad.lines(ax1, x, y, color='blue', thickness=3)
    cad.points(ax1, x, y, color='red')
    cad.pause()

    print('Good job!')
    
if __name__ == "__main__":
    main() 
