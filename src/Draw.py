import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.cm as cm
import matplotlib.patches as patches
from matplotlib.path import Path

def line(ax,x1,y1,x2,y2,color='black',alpha=0.5):
    l = patches.Polygon([(x1,y1), (x2,y2)], linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
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
