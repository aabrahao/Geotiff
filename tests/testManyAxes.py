import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.cm as cm
import matplotlib.patches as patches
from matplotlib.path import Path

# Fixing random state for reproducibility
np.random.seed(19680801)

class Line (patches.Polygon):
    def set_points(self,x1,y1,x2,y2):
        l.set_xy([(x1,y1),(x2,y2)])


def line(x1,y1,x2,y2, color='black',alpha=0.5):
    l = Line([(x1,y1), (x2,y2)], linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax = plt.gca()
    ax.add_patch(l)
    return l

def circle(x,y,r, color='black',alpha=0.5):
    c = patches.Circle((x,y), r, linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax = plt.gca()
    ax.add_patch(c)
    return c

def rectangle(x,y,w,h, color='black',alpha=0.5):
    r = patches.Rectangle((x,y), w, h, rotation_point='center', linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
    ax = plt.gca()
    ax.add_patch(r)
    return r


delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, axs = plt.subplots(1,3,figsize=(18,18))
im = axs[0].imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-3, 3, -3, 3],
               vmax=abs(Z).max(), vmin=-abs(Z).max())


l = line(-3,-3,3,-3)
c = circle(0,0,.1,color='red')
r = rectangle(0,0,.5,.75)
rectangle(0,0,.5,.75)

axs[0].set_xlim(-10,10)
axs[0].set_ylim(-10,10)

plt.pause(1)


if c.contains_point((0,0),c.get_radius()):
    print('Contains')
else:
    print('Do not contain!')

for i in range(3):
    print(i)
    c.set_center((i,i))
    l.set_points(-3,i,3,i)
    r.set_angle(i*45)
    plt.pause(1)


plt.show()
