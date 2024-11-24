import System as sys
import Geotiff as gt

def main(): 
    files = sys.list('data/examples/*.tif*')
    for file in files:
        dataset = gt.Dataset( file )
        dataset.info()
        dataset.show(block=True)
    sys.pause()
    
if __name__ == "__main__":
    main()
    