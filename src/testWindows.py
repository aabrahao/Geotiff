import System as sys
import Geotiff as gt
import numpy as np
import Cad as drw
import matplotlib.pyplot as plt
import Print as prt

def show(ax, z):
    ax.imshow(z)
    ax.set_aspect('equal', adjustable='box')

def main():

    image = gt.Dataset('data/rifle/satellite.tif')
    x,y,w,h = image.bounds()

    fig, ax1 = plt.subplots(figsize=(30,28))
    image.show(ax=ax1)
    plt.pause(0.01)


    fig, (ax2, ax3) = plt.subplots(1, 2, figsize=(30,28))

    ax2.set_xlim(x, x + w)
    ax2.set_ylim(y, y + h)

    n = 50
    m = 50

    dw = w/n
    dh = h/m
    
    plt.pause(.001)

    for j in range(0, m):
        for i in range(0,n):
            prt.field('Tile', (j,i))
            z = gt.Dataset('data/rifle/terrain-masked.tif', x + i*dw, y + j*dh, dw, dh)
            z.draw(ax1, 'red', .25)
            z.show(ax=ax2)
            ax3.clear()
            z.show(ax=ax3)
            plt.pause(.001)

    plt.show()

    print('Good job!')
    
if __name__ == "__main__":
    main() 
