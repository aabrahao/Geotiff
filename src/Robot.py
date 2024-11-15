import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
import matplotlib.patches as patches

class Robot:
    def __init__(self, x, y):
        self.particle = Particle(x,y,'red',True)
        self.chasis = patches.Rectangle((x - 0.5*5.5, y - 0.5*3.7), 5.5, 3.7, linewidth=1, edgecolor='blue', facecolor='blue', alpha=0.5)
        self.lidar = rect = patches.Rectangle((x + 4.3, y - 0.5*30), 18, 30, linewidth=1, edgecolor='orange', facecolor='orange', alpha=0.5)
        ax = plt.gca()
        #ax.add_patch(self.chasis)
        #ax.add_patch(self.lidar)
    def move(self, x, y, v):
        self.particle.move(x,y)
        if np.sign(v) < 0:
            self.chasis.set_xy((x - 0.5*5.5, y - 0.5*3.7))
            self.lidar.set_xy((x - 4.3 - 18,y - 0.5*30))
        else:
            self.chasis.set_xy((x - 0.5*5.5, y - 0.5*3.7))
            self.lidar.set_xy((x + 4.3,y - 0.5*30))

    def inside(self,x,y,r):
        return self.particle(x,y,r)
    