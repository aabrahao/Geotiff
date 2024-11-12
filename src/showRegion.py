import System as sys
import Geotiff as gt
import Grid as gd
import numpy as np

def toFoot(m):
    return 3.28084*m

def toMeter(ft):
    return ft/3.28084

def main():

    #satellite = gt.open('data/rifle/satellite.tif')
    #gt.info(satellite)
    #gt.show(satellite)

    terrain = gt.open('data/rifle/terrain-masked.tif')
    gt.info(terrain)
    r = gt.show(terrain)
    
    x,y,z = gt.grid(terrain, nodata = True)
    zmin, zmax = gd.range(z)
    print('Elevation:', toFoot(zmax-zmin),'ft')
    
    ux, uy = gd.gradient(x,y,z)
    u = np.sqrt(np.power(ux,2) + np.power(uy,2))
        
    if not r:
        print('Show all!')
    else:
        xr,yr,wr,hr = r
        print(f'Show area:({xr},{yr}),{wr},{hr}!')
        i1, j1 = terrain.index(xr,yr)
        i2, j2 = terrain.index(xr+wr,yr+hr)
        i1, i2 = gd.normalize(i1,i2)
        j1, j2 = gd.normalize(j1,j2)

        x = x[i1:i2,j1:j2]
        y = y[i1:i2,j1:j2]
        z = z[i1:i2,j1:j2]
        u = u[i1:i2,j1:j2] 

    gd.show(x,y,z)
    gd.show(x,y,u)
    
    sys.pause()
    
if __name__ == "__main__":
    main() 