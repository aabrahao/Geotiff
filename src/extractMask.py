import System as sys
import Geotiff as gt
import Grid as gd
import numpy as np
from random import random 
import rasterio as rio

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def rand(rmin=0.0, rmax=1.0):
    return (rmax-rmin)*random() + rmin

def toFoot(m):
    return 3.28084*m

def toInch(m):
    return m*39.3701

def toMeter(ft):
    return ft/3.28084

def line(ax,x1,y1,x2,y2, color='black',alpha=0.5):
    l = patches.Polygon([(x1,y1), (x2,y2)], linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax.add_patch(l)
    return l

def main():
    
    # Geotiff
    rgb = gt.open('data/rifle/satellite.tif')
    z = gt.open('data/rifle/terrain-masked.tif')
    dx, dy = gt.resolution(rgb)

    print('Model')
    print(f'Resolution: {toInch(dx)} x {toInch(dy)} inches')
    
    # Fence
    xf, yf = gt.mask('data/rifle/satellite-masked.tif')
    # Safe boundory
    xb, yb = gd.offset(xf,yf,toMeter(-30))
    bxmin, bxmax = gd.range(xb)
    bymin, bymax = gd.range(yb)
    
    # Drawings
    fig = plt.figure(figsize=(28,18))
    
    axi = plt.subplot(121)
    gt.show(rgb, axes=axi)
    axi.plot(xf, yf, linewidth=3.0, color='green', alpha = 1)
    axi.plot(xb, yb, linewidth=3.0, color='red', alpha = 1)
    plt.pause(.1)
    
    axe = plt.subplot(222)
    gt.show(z, axes = axe)
    axe.plot(xf, yf,linewidth=3.0, color='green', alpha = 1)
         
    axl = plt.subplot(224)
    
    # Grid
    df = toMeter(30)
    for yg in np.arange(bymin, bymax, df):
        line(axi, bxmin,yg,bxmax,yg)
    
    plt.show()
    
if __name__ == "__main__":
    main() 