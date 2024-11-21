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

# (left, bottom, width, height) (this is called "bounds" in matplotlib); or
# (left, bottom, right, top) (called "extent").

class Region:
    def __init__(self, filename, x=None, y=None, wx=None, wy=None):
        self.filename = filename
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy
        self.update()
    def update(self):
        with open(self.filename) as dataset:
            # Region
            if self.x is None:
                self.x = dataset.bounds.left
            if self.y is None:
                self.y = dataset.bounds.right
            if self.wx is None:
                self.wx = dataset.bounds.right  - dataset.bounds.left
            if self.wy is None:
                self.wy = dataset.bounds.bottom - dataset.bounds.top
            # Dataset            
            self.dx, self.dy = resolution(dataset)
            self.nx, self.ny = size(dataset)
            self.transform = dataset.transform
    def info(self):
        prt.section('Region')
        prt.field('Origin:', (self.x, self.y))
        prt.field('Width:', (self.wx, self.wy))        
        with open(self.filename) as dataset:
            info(dataset)
    def data(self, band = 1):
        with open(self.filename) as dataset:
            return data(dataset, band)
    def mask(self):
        with open(self.filename) as dataset:
            m = mask(dataset)
        return m
    def show(self, colormap = cm.gist_earth, axes=None, block=False):
        with open(self.filename) as dataset:
            show(dataset, colormap, axes, block=block)
    def fence(self, band = 1):
        with open(self.filename) as dataset:
            x,y = fence(dataset, band)
        return x,y

def bounds(dataset):
    xmin = dataset.bounds.left
    xmax = dataset.bounds.right
    ymin = dataset.bounds.top
    ymax = dataset.bounds.bottom
    return xmin, ymin, xmax, ymax

def size(dataset):
    nx = dataset.height
    ny = dataset.width
    return nx, ny

def width(dataset):
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

# Printers...

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
    prt.field('Bounds', bounds(dataset))
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

def data(dataset, band = 1):
    d = dataset.read(band)
    if np.issubdtype(d.dtype, np.floating):
        m = dataset.read_masks(band)
        d[m==0] = np.nan
    return d

def mask(dataset, band = 1):
    m = dataset.read_masks(band)
    m = m.astype(np.float32)
    m[m==0] = 0.0
    m[m==255] = 1.0
    return m

def fence(dataset, band = 1):
    m = mask(dataset, band)
    contours = find_contours(m, 0.5)
    n = len(contours) 
    if n == 0:
        print('Ops, no geofence found!')
        return np.array([]), np.array([])
    elif n > 1:
        print('Ops, multiple geofence found and ignored!')
    # World
    c = contours[0]
    i = c[:, 1]
    j = c[:, 0]
    x,y = transform.xy(dataset.transform, j,i)
    return np.array(x), np.array(y)

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
