from rasterio import open
from pprint import pprint
import rasterio.plot as rplt
from rasterio import transform
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets  import RectangleSelector

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

from skimage import measure

g_figure_size = (18, 18) # Inches
g_surface_count = 200 # Points
g_selected_rectangle = []

def size(dataset):
    nx = dataset.height
    ny = dataset.width
    return nx, ny

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

def nodata(database):
    return database.nodata

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

def show(dataset, colormap = cm.gist_earth, axes = None):
    # Axes
    if not axes:
        fig = plt.figure(figsize=g_figure_size)
        ax = fig.add_subplot(1,1,1)
    else:
        ax = axes
    # Image or elevation?    
    if dataset.count == 1:
        rplt.show(dataset, ax=ax, cmap = colormap)
    else:
        rplt.show(dataset, ax=ax)
    # Decoration
    plt.tight_layout()
    plt.grid()
    # Show
    if not axes:
        plt.show()
    # Return ax for decoration
    return ax

def grid(dataset, band=1, nodata=False):
    xmin, ymin, xmax, ymax = bounds(dataset)
    n,m = size(dataset)
    x = np.linspace( xmin, xmax, n)
    y = np.linspace( ymin, ymax, m)
    x, y = np.meshgrid(x, y) 
    z = dataset.read(band)
    if nodata:
        z[z==dataset.nodata] = np.nan
    return x, y, z

def mask(filename):
    dataset = open(filename)
    # Image or elevation
    if dataset.count == 4:
        mask = dataset.read(4)
        mask[mask==0] = 0.0
        mask[mask==255] = 1.0
    else:
        print('Ops, no mask implemented for elevatio, only rgb image')
        return None
    # Extract contourns
    contours = measure.find_contours(mask, 0.5)[0]
    i = contours[:, 1]
    j = contours[:, 0]
    x,y = transform.xy(dataset.transform, j,i)
    return np.array(x), np.array(y)
