import System as sys
import Geotiff as gt
import matplotlib.pyplot as plt
import numpy as np

def main(): 
    files = sys.list('data/examples/*.tif*')
    print(files)
    for file in files:
        dataset = gt.open( file )
        gt.info(dataset)
        gt.show(dataset)
    sys.pause()
    
if __name__ == "__main__":
    main()
    