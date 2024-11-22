import Default as dft

from rasterio import open
import rasterio.plot as rplt
from rasterio import transform
from rasterio.windows import Window
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets  import RectangleSelector

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

from skimage.measure import find_contours

import Print as prt

# Matrix index               |  World coordnates
#                            |
# Window: (i, j), w, h       |  Area: (x, y), w, h
#    +--- i                  |    y        +----+ e
#    |         1 +----+      |    |        |    |
#    |           |    |      |    |      o +----+ 
#    j           +----+ 2    |    +--- x    
#                            |
 
# Bound : x, y, w, h
# Extent: xmin, ymin, xmax, ymax.

#############################################################
# Dataset

def world(dataset, i, j):
    x,y = transform.xy(dataset.transform, i, j)
    return x, y

def index(dataset, x, y):
    i, j = dataset.index(x, y)
    return i, j

def window(dataset, x, y, w, h):
    i1, j1 = index(dataset, x, y + h)
    i2, j2 = index(dataset, x + w, y)
    return i1, j1, i2 - i1, j2 - j1

def area(dataset, i, j, w, h):
    xo, yo = world(dataset, i, j + h)
    xe, ye = world(dataset, i + w, j) 
    return xo, yo, xe - xo, ye - yo

def extents(dataset):
    xmin = dataset.bounds.left
    xmax = dataset.bounds.right
    ymin = dataset.bounds.bottom
    ymax = dataset.bounds.top
    return xmin, ymin, xmax, ymax

def bounds(dataset):
    xmin, ymin, xmax, ymax =  extents(dataset)
    return xmin, ymin, xmax - xmin, ymax - ymin

def size(dataset):
    n = dataset.height
    m = dataset.width
    return n, m

def width(dataset):
    xmin, ymin, xmax, ymax = extents(dataset)
    return xmax - xmin, ymax - ymin

def origin(dataset):
    tx = dataset.transform[2]
    ty = dataset.transform[5]
    return tx, ty

def resolution(dataset):
    sx = dataset.transform[0]
    sy = -dataset.transform[4]
    return sx, sy

def info(dataset):
    prt.section('Dataset')
    prt.field('File', dataset.name)
    prt.field('Driver', dataset.driver)
    prt.field('Mode', dataset.mode)
    prt.field('Size', size(dataset))
    prt.field('Bands', dataset.count)
    prt.field('Indexes', dataset.indexes)
    prt.field('Types', dataset.dtypes)
    prt.field('Nodata', dataset.nodata)
    prt.field('Coordnates', dataset.crs)
    prt.section('Geometry')
    #prt.field('Units', dataset.crs.linear_units)
    prt.field('Extents', extents(dataset))
    prt.field('Resolution', resolution(dataset))
    prt.field('Origin', origin(dataset))
    prt.field('Width', width(dataset))
    prt.section('Transform')
    prt.field(dataset.transform)
    #prt.section('Profile')
    #prt.json(dataset.profile)
    prt.section()

def show(dataset, colormap = cm.gist_earth, axes = None, block=False):
    if not axes:
        fig, ax = plt.subplots(figsize = dft.figureSize())
        ax.set_title(dataset.name)
    else:
        ax = axes
    if dataset.count == 1:
        rplt.show(dataset, ax=ax, cmap = colormap)
    else:
        rplt.show(dataset, ax=ax)
    plt.tight_layout()
    plt.grid()
    if not axes:
        plt.show(block=block)
    return ax

def data(dataset, band = 1, window=None):
    if window is None:
        n,m = size(dataset)
        window = Window(0,0,n,m)
    d = dataset.read(band, window=window)
    if np.issubdtype(d.dtype, np.floating):
        m = dataset.read_masks(band, window=window)
        d[m==0] = np.nan
    return d

def mask(dataset, band = 1, window=None):
    if window is None:
        n,m = size(dataset)
        window = Window(0,0,n,m)
    m = dataset.read_masks(band, window=window)
    m = m.astype(np.float32)
    m[m==0] = 0.0
    m[m==255] = 1.0
    return m

def boundary(dataset, band = 1, window=None):
    if window is None:
        n,m = size(dataset)
        window = Window(0,0,n,m)
    m = mask(dataset, band, window)
    contours = find_contours(m, 0.5)
    n = len(contours) 
    if n == 0:
        print('Ops, boundary not found!')
        return np.array([]), np.array([])
    elif n > 1:
        print('Ops, multiple boundaries found; first one considered!')
    # World
    c = contours[0]
    i = c[:, 1]
    j = c[:, 0]
    x,y = transform.xy(dataset.transform, j,i)
    return np.array(x), np.array(y)

def grid(dataset, band=1, nodata=False):
    xmin, ymin, xmax, ymax = extents(dataset)
    n,m = size(dataset)
    x = np.linspace( xmin, xmax, n)
    y = np.linspace( ymin, ymax, m)
    x, y = np.meshgrid(x, y) 
    z = dataset.read(band)
    if nodata:
        z[z==dataset.nodata] = np.nan
    return x, y, z

#############################################################
# Region

class Region:
    def __init__(self, filename, x=None, y=None, w=None, h=None):
        self.filename = filename
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.update()
    def update(self):
        with open(self.filename) as dataset:
            x, y, w, h = bounds(dataset)
            # Region
            if self.x is None:
                self.x = x
            if self.y is None:
                self.y = y
            if self.w is None:
                self.w = w
            if self.h is None:
                self.h = h
            # Dataset            
            self.dx, self.dy = resolution(dataset)
            self.n, self.m = size(dataset)
            self.transform = dataset.transform
    def window(self, dataset):
        i,j,w,h = window(dataset, self.x, self.y, self.w, self.w)
        return Window(i,j,w,h)
    def info(self):
        prt.section('Region')
        prt.field('Origin:', (self.x, self.y))
        prt.field('Width:', (self.w, self.h))        
        with open(self.filename) as dataset:
            info(dataset)
    def data(self, band = 1):
        with open(self.filename) as dataset:
            return data(dataset, band, window=self.window(dataset))
    def mask(self):
        with open(self.filename) as dataset:
            m = mask(dataset)
        return m
    def boundary(self, band = 1):
        with open(self.filename) as dataset:
            x,y = boundary(dataset, band)
        return x,y
    # World
    def bounds(self):
        return self.x, self.y, self.w, self.h 
    def extents(self):
        return self.x, self.y, self.x + self.w, self.y + self.h
    def origin(self):
        return self.x, self.y
    def width(self):
        return self.w, self.h
    def world(self, i, j):
        x,y = transform.xy(self.transform, i, j)
        return x, y
    # Index
    def size(self):
        return self.n, self.m
    def index(self, x, y):
        i, j = transform.index(self.transform, x, y)
        return i, j
    def show(self, colormap = cm.gist_earth, axes=None, block=False):
        with open(self.filename) as dataset:
            show(dataset, colormap, axes, block=block)
