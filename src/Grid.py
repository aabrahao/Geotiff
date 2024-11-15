import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets  import RectangleSelector

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

g_figure_size = (18, 18) # Inches
g_surface_count = 200 # Points
g_selected_rectangle = []

# (left, bottom, width, height) (this is called "bounds" in matplotlib); or
# (left, bottom, right, top) (called "extent").

def error(actual, observed):
    return np.abs((observed - actual)/actual)*100

def printError(actual, observed):
    print('|', actual,' - ', observed, '| = ', np.abs(observed - actual), ' ', error(actual, observed), '%')

def range(x):
    xmin = np.nanmin(x)
    xmax = np.nanmax(x)
    return xmin, xmax

def normalize(i1, i2):
    return min(i1, i2), max(i1, i2)

def clamp(vmin, v, vmax):
    v = max(vmin, v)
    v = min(v, vmax)
    return v

def gradient(x,y,z):
    dx = x[0,1] - x[0,0]
    dy = y[1,0] - y[0,0]
    print('d:', dx, dy)
    gx, gy = np.gradient(z, dx, dy)
    return gx, gy 

def show(x, y=[], z=[], colormap = cm.jet, block=False):
    fig = plt.figure(figsize=g_figure_size)
    ax = fig.add_subplot()
    if not y or not z:
        ax.imshow(x, cmap=colormap)
    else:
        ax.imshow(z, cmap=colormap)
    ax.set_axis_off()
    ax.grid()
    plt.show(block=block)

def plot(x, y, z, colormap = cm.jet, block=False):
    fig = plt.figure(figsize=g_figure_size)
    ax = fig.add_subplot(projection='3d', proj_type = 'ortho')
    ax.plot_surface(x, y, z, cmap=colormap,
                    linewidth=0,
                    antialiased=False,
                    edgecolors='k',
                    rcount = g_surface_count,
                    ccount = g_surface_count)
    ax.set_position([0, 0, 1, 1])
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.view_init(90, -90, 0)
    ax.set_aspect('equal')
    plt.tight_layout()
    ax.set_axis_off()
    plt.show(block=block)

def contour(x, y, z, levels = 50, colormap = cm.jet, block=False):
    fig = plt.figure(figsize=g_figure_size)
    ax = fig.add_subplot()
    ax.contour(x, y, z, levels = levels,
               colors = "k",
               linewidth=0,
               antialiased=False)
    ax.contourf(x, y, z, levels=levels, cmap=colormap,
                alpha = 0.75,
                rcount = g_surface_count,
                ccount = g_surface_count,
                linewidth=0,
                antialiased=False)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.grid()
    plt.show(block=block)
