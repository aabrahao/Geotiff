import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.cm as cm
import matplotlib.patches as patches
from matplotlib.path import Path

def line(ax,x1,y1,x2,y2,color='black',alpha=0.5):
    l = patches.Polygon([(x1,y1), (x2,y2)], linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax = plt.gca()
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

def main():
    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2) * 2

    fig, ax = plt.subplots()
    im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
                   origin='lower', extent=[-3, 3, -3, 3],
                   vmax=abs(Z).max(), vmin=-abs(Z).max())


    l = line(ax, -3,-3,3,-3)
    c = circle(ax, 0,0,.1,color='red')
    r = rectangle(ax, 0,0,.5,.75)
    rectangle(ax, 0,0,.5,.75)

    plt.pause(1)
    plt.show()

if __name__ == "__main__":
    main() 