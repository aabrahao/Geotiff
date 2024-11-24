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

    image = gt.open('data/rifle/satellite.tif')
    gt.info(image)

    x,y,w,h = gt.bounds(image)

    z = gt.Dataset('data/rifle/terrain-masked.tif',x+w/2,y+h/2,w/2,h/2)
    #z = gt.Dataset('data/rifle/terrain-masked.tif',x,y,w,h)
    z.info()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30,28))
    
    gt.show(image,ax=ax1)
   
    xz,yz = z.origin()
    wz,hz = z.width()
    drw.circle(ax1,xz,yz,100,color='red')
    drw.circle(ax1,xz+wz,yz+hz,100,color='red')
    drw.line(ax1,xz,yz,xz+wz,yz+hz,color='red')
    drw.rectangle(ax1,xz,yz,wz,hz)

    prt.field('Origin', z.toWorld(0,0))
    xb, yb = z.toWorld(0,0)
    xe, ye = z.toWorld(5597, 4935)
    drw.circle(ax1,xb,yb,100,color='green')
    drw.circle(ax1,xe,ye,100,color='green')
    drw.line(ax1,xb,yb,xe,ye,color='red')
       
    prt.field('left,bottom  (h,0)', z.fromWorld(xz,yz))
    prt.field('left,top     (0,0)', z.fromWorld(xz,yz+hz))
    prt.field('right,top    (0,w)', z.fromWorld(xz+wz,yz+hz))
    prt.field('right,bottom (h,w)', z.fromWorld(xz+wz,yz))

    n, m = gt.size(image)
    prt.field('wx: widht' , n)
    prt.field('wy: height', m)

    prt.field('Window start:', z.fromWorld(xz,yz+hz))
    prt.field('Window end:', z.fromWorld(xz+wz,yz))

    drw.circle(ax1,xz,yz+hz, 50, color='red')
    drw.circle(ax1,xz,yz, 50, color='green')
    drw.circle(ax1,xz+wz,yz, 50, color='blue')
    drw.circle(ax1,xz+wz,yz+hz, 50, color='magenta')

    z.show(ax=ax2)

    plt.show()
    
if __name__ == "__main__":
    main() 
