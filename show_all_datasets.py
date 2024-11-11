import glob
from rasterio import open
from rasterio.plot import show
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

def error(actual, observed):
    return np.abs((observed - actual)/actual)*100

def printError(actual, observed):
    print('|', actual,' - ', observed, '| = ', np.abs(observed - actual), ' ', error(actual, observed), '%')

def wait():
    print("Press any key to continue...")
    input()

def list(pattern):
    return glob.glob(pattern)

def size(dataset):
    n = dataset.width
    m = dataset.height
    return n, m

def bounds(dataset):
    xmin = dataset.bounds.left
    xmax = dataset.bounds.right
    ymin = dataset.bounds.top
    ymax = dataset.bounds.bottom
    return xmin, ymin, xmax, ymax

def length(dataset):
    xmin, ymin, xmax, ymax = bounds(dataset)
    w = xmax - xmin
    h = ymax - ymin
    return w, h

def origin(dataset):
    x = dataset.transform[2]
    y = dataset.transform[5]
    return x, y

def resolution(dataset):
    sx = dataset.transform[0]
    sy = -dataset.transform[4]
    return sx, sy

def info(dataset):
    nx, ny = size(dataset)
    lx, ly = length(dataset)
    dx, dy = resolution(dataset)
    x, y = origin(dataset)
    print('-----------------------')
    print('File:', dataset.name)
    print('Driver:', dataset.driver)
    print('Mode:', dataset.mode)
    print('Size:', nx, 'x', ny)
    print('Bands:', dataset.count)
    print('Indexes:', dataset.indexes)
    print('Coordnates:', dataset.crs)
    #print('Units:', dataset.crs.linear_units)
    print('Bounds:', bounds(dataset))
    print('Transform:')
    print(dataset.transform)
    print('Resolution:',dx,'x',dy )
    print('Origin:(',lx,',',ly,')')
    print('Length:',lx,'x',ly)
    print('Nodata', dataset.nodata)
    pprint(dataset.profile)

def grid(dataset, band=1):
    xmin, ymin, xmax, ymax = bounds(dataset)
    n,m = size(dataset)
    xr = np.linspace( xmin, xmax, n)
    yr = np.linspace( ymin, ymax, m)
    x, y = np.meshgrid(xr, yr) 
    z = dataset.read(band)
    return x, y, z

def plot(x,y,z):
    plt.figure()
    plt.imshow(z, cmap = 'jet')
    plt.show(block=False)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d', proj_type = 'ortho')
    ax.plot_surface(x, y, z, cmap='jet',linewidth=0, antialiased=False)
    ax.set_position([0, 0, 1, 1])
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.view_init(90, -90, 0)
    ax.set_aspect('equal')

    plt.grid()
    plt.show()

def annotate(dataset, block = False):
    fig = plt.figure(figsize=(18,18))
    ax = fig.add_subplot(1,1,1)

    if dataset.count == 1:
        show(dataset, ax=ax, cmap = 'Greys_r')
    else:
        show(dataset, ax=ax)

    plt.tight_layout()
    plt.show(block=block)

def main(): 
    files = list('rifle/*.tif*')
    for file in files:
        dataset = open( file )
        info(dataset)
        annotate(dataset, True)
    wait()
    
if __name__ == "__main__":
    main()