import System as sys
import Geotiff as gt
import Grid as gd
import numpy as np

def toFoot(m):
    return 3.28084*m

def toMeter(ft):
    return ft/3.28084

def main():
    satellite = gt.open('data/rifle/satellite.tif')
    gt.info(satellite)
    gt.show(satellite)

    terrain = gt.open('data/rifle/terrain-masked.tif')
    gt.info(terrain)
    gt.show(terrain)
    
    x,y,z = gt.grid(terrain, nodata = True)
    gd.plot(x,y,z)
    
    zmin, zmax = gd.range(z)
    print('Elevation:', toFoot(zmax-zmin),'ft')
    
    ux, uy = gd.gradient(x,y,z)
    u = np.sqrt(np.power(ux,2) + np.power(uy,2))
    gd.plot(x,y,u)

    print('------------------------------------')
    print('Satellite:', satellite.shape)
    print('Terrain:', terrain.shape)
    print('x:', x.shape)
    print('y:', y.shape)
    print('z:', z.shape)
    print('ux:', ux.shape)
    print('uy:', uy.shape)
    print('u:', u.shape)
    print('------------------------------------')

    sys.pause()
    
if __name__ == "__main__":
    main() 