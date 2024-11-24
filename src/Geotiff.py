import Settings as dft

from rasterio import open

from rasterio import transform
from rasterio.plot import show
from rasterio.windows import Window
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets  import RectangleSelector

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

from skimage.measure import find_contours

import Print as prt
import Cad as drw
import Geometry as gmt

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

class Dataset:
    def __init__(self, name, x=None, y=None, w=None, h=None):
        self.name = name
        with open(self.name) as dataset:
            self.x, self.y, self.w, self.h = bounds(dataset)
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y
            if w is not None:
                self.w = w
            if h is not None:
                self.h = h
            self.transform = dataset.transform
    ##############################################################################################
    # Info
    def info(self):
        prt.section('Region')
        prt.field('Origin:', (self.x, self.y))
        prt.field('Width:', (self.w, self.h))        
        with open(self.name) as dataset:
            info(dataset)
    ##############################################################################################
    # World
    def bounds(self):
        return self.x, self.y, self.w, self.h 
    def extents(self):
        return self.x, self.y, self.x + self.w, self.y + self.h
    def origin(self):
        return self.x, self.y
    def width(self):
        return self.w, self.h
    def toWorld(self, i, j):
        return toWorld(self.transform, i, j)
    ##############################################################################################
    # Data 
    def window(self):
        return window(self.transform, self.x, self.y, self.w, self.h)
    def fromWorld(self, x, y):
        return fromWorld(self.transform, x, y)
        
    def data(self, band = 1):
        with open(self.name) as dataset:
            d = dataset.read(band, window = self.window())
            if np.issubdtype(d.dtype, np.floating):
                m = dataset.read_masks(band, window = self.window())
                d[m==0] = np.nan
        return d
    ##############################################################################################
    # Visualization
    def show(self, ax=None, colormap = cm.gist_earth, block=False):
        with open(self.name) as dataset:
            if not ax:
                fig, axes = plt.subplots(figsize = dft.figureSize())
                axes.set_title(dataset.name)
            else:
                axes = ax
            if dataset.count == 1:
                z = self.data()
                axes.imshow(z, cmap = colormap, aspect='equal',
                          extent=(self.x, self.x + self.w, self.y, self.y + self.h) )
                # , interpolation='bilinear'
                axes.set_aspect('equal')
                #axes.set_adjustable('box')
            else:
                show(dataset, ax=axes)
            if not ax:
                plt.show(block=block)
            return ax
    def grid(self, band=1):
        xmin, ymin, xmax, ymax = self.extents()
        z = self.data(band)
        m, n = z.shape
        x = np.linspace( xmin, xmax, n)
        y = np.linspace( ymin, ymax, m)
        x, y = np.meshgrid(x, y)
        return x, y, z
    def surface(self, ax=None, colormap = cm.jet, block=False):
        with open(self.name) as dataset:
            if not ax:
                fig, axes = plt.subplots(figsize = dft.figureSize())
                axes.set_title(dataset.name)
            else:
                axes = ax
            if dataset.count == 1:
                x,y,z = self.grid()
                n, m = z.shape
                n = min(n, 200)
                m = min(m, 200)
                ax.plot_surface(x, y, z, cmap = colormap, rcount = n, ccount = m, lw=0.5) #, alpha=0.5)
                axes.set_aspect('equal')
                #axes.set_adjustable('box')
            else:
                show(dataset, ax=axes)
            if not ax:
                plt.show(block=block)
            return ax
    ##############################################################################################
    # Visualization
    def draw(self, ax, color = 'red', alpha = 0.5 ):
        r = drw.rectangle(ax, self.x, self.y, self.w, self.h, color, alpha)
    ##############################################################################################
    # Boundary
    def mask(self, band = 1):
        with open(self.name) as dataset:
            m = dataset.read_masks(band, window = self.window())
        m = m.astype(np.float32)
        m[m==0] = 0.0
        m[m==255] = 1.0
        return m
    def boundary(self, band = 1):
        m = self.mask(band)
        contours = find_contours(m, 0.5)
        n = len(contours) 
        if n == 0:
            print('Ops, boundary not found!')
            return gmt.fromList([]), gmt.fromList([])
        elif n > 1:
            print('Ops, multiple boundaries found and ignored!')
        c = contours[0]
        i = c[:, 0]
        j = c[:, 1]
        x,y = self.toWorld(i, j)
        return gmt.fromList(x), gmt.fromList(y)

##############################################################################################
# Helpers

def toWorld(tf, i, j):
    return transform.xy(tf, i, j)

def fromWorld(tf, x, y):
    return transform.rowcol(tf, xs=x, ys=y)

def window(tf, x, y, w, h):
    i1, j1 = fromWorld(tf, x, y + h)
    i2, j2 = fromWorld(tf, x + w, y)
    return Window(j1, i1, j2 - j1, i2 - i1)

def area(dataset, i, j, w, h):
    xo, yo = toWorld(dataset, i, j + h)
    xe, ye = toWorld(dataset, i + w, j) 
    return xo, yo, xe - xo, ye - yo

def extents(dataset):
    xmin = dataset.bounds.left
    xmax = dataset.bounds.right
    ymin = dataset.bounds.bottom
    ymax = dataset.bounds.top
    return xmin, ymin, xmax, ymax

def bounds(dataset):
    x, y = origin(dataset)
    w, h = width(dataset)
    return x, y, w, h

def size(dataset):
    iw = dataset.height
    jw = dataset.width
    return iw, jw

def width(dataset):
    xmin, ymin, xmax, ymax = extents(dataset)
    return xmax - xmin, ymax - ymin

def origin(dataset):
    xmin, ymin, xmax, ymax = extents(dataset)
    return xmin, ymin

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
    prt.field('Units', dataset.crs.linear_units)
    prt.field('Extents', extents(dataset))
    prt.field('Resolution', resolution(dataset))
    prt.field('Origin', origin(dataset))
    prt.field('Width', width(dataset))
    prt.section('Transform')
    prt.field(dataset.transform)
    prt.section('Profile')
    prt.json(dataset.profile)
    prt.section()