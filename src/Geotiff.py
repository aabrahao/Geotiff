from rasterio import open
from pprint import pprint
import rasterio.plot as rplt
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets  import RectangleSelector

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

g_figure_size = (18, 18) # Inches
g_surface_count = 200 # Points
g_selected_rectangle = []

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

def show(dataset, colormap = cm.gist_earth, block=True):
    global g_selected_rectangle
    fig = plt.figure(figsize=g_figure_size)
    ax = fig.add_subplot(1,1,1)
    if dataset.count == 1:
        rplt.show(dataset, ax=ax, cmap = colormap)
    else:
        rplt.show(dataset, ax=ax)
    plt.tight_layout()
    plt.grid()

    g_selected_rectangle = []
    def showSelectorCallback(eclick, erelease):
        global g_selected_rectangle
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        x = min(x1,x2)
        y = min(y1,y2)
        w = np.abs(x1-x2)
        h = np.abs(y1-y2)
        g_selected_rectangle = [x,y,w,h]
    rs = RectangleSelector(ax, showSelectorCallback, 
                           drawtype='box', useblit=False, button=[1], 
                           minspanx=5, minspany=5, spancoords='data', 
                           interactive=True)

    plt.show(block=block)
    return g_selected_rectangle

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
