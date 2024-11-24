import System as sys
import Geotiff as gt
import numpy as np
import Cad as drw
import matplotlib.pyplot as plt
import Print as prt

def read(x,y,w,h):
    with gt.open('data/rifle/drone.tif') as dataset:
        print(gt.size(dataset))
        z = dataset.read(window = gt.Window(0, 0, 3000, 3000))
    return z[0]
    
def main():

    terrain = gt.Dataset('data/rifle/drone.tif')
    terrain.info()

    x,y,w,h = terrain.bounds()

    with gt.open('data/rifle/drone.tif') as dataset:
        print(gt.size(dataset))
        z = dataset.read(window = gt.Window(0, 0, 3000, 3000))
    
    #z = z[0]
    #print(z)
    #prt.array(z)
    #plt.imshow(z)
    #plt.show()
    
    
if __name__ == "__main__":
    main() 
