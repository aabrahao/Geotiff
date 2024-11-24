import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.cm as cm
import matplotlib.patches as patches
from matplotlib.path import Path

import Settings as stg

def plots(rows = 1, cols = 1):
    fig, axes = plt.subplots(rows, cols, figsize = stg.figureSize() )
    return axes

def update():
    plt.pause(0.01)
    plt.show(block=False)

def pause():
    plt.show(block=True)

def clear(ax):
    ax.clear()

def limits(ax, x = None, y = None, w = None, h = None, bounds = None, extents = None):
    if None not in (x, y, w, h):
        ax.set_xlim(x, x + w)
        ax.set_ylim(y, y + h)
    elif bounds is not None:
        x, y, w, h = bounds
        ax.set_xlim(x, x + w)
        ax.set_ylim(y, y + h)
    elif extents is not None:
        x, y, xe, ye = extents
        ax.set_xlim(x, xe)
        ax.set_ylim(y, ye)

def title(ax, title):
    ax.set_title(title)

def point(ax,x,y,color='black', alpha=0.5):
    p = ax.plot([x], [y], color=color, alpha=alpha, linewidth = 1, marker='o')
    return p

def line(ax,x1,y1,x2,y2,color='black',thickness = 1, alpha=0.5):
    l = patches.Polygon([(x1,y1), (x2,y2)], 
                        linewidth=thickness,
                        edgecolor=color, 
                        facecolor=color, 
                        alpha=alpha)
    ax.add_patch(l)
    return l

def circle(ax,x,y,r,color='black',alpha=0.5):
    c = patches.Circle((x,y), r, linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax.add_patch(c)
    return c

def rectangle(ax,x,y,w,h,color='black',alpha=0.5):
    r = patches.Rectangle((x,y), w, h, rotation_point='center', linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax.add_patch(r)
    return r

def points(ax, x, y, color='black', alpha=0.5):
    c = ax.plot(x, y, color=color, alpha=alpha, linewidth = 1, marker='o')
    return c

def lines(ax, x, y, color='black', thickness=3, marker=None, alpha=0.5):
    c = ax.plot(x, y, color=color, alpha=alpha, linewidth = thickness, marker=marker)
    return c

def dataset(ax, data):
    data.show(ax)

