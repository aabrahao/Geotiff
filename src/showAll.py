import System as sys
import Geotiff as gt
import matplotlib.pyplot as plt
import numpy as np

def main(): 
    files = sys.list('data/rifle/*.tif*')
    for file in files:
        dataset = gt.open( file )
        gt.info(dataset)
        gt.show(dataset,block=False)
    sys.pause()
    
if __name__ == "__main__":
    main()
    