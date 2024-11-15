#!/usr/bin/env python

# Particle simulation
# FIU-ARC
# Summer 2024

import numpy as np
import matplotlib.pyplot as plt
from random import random 

def rand(rmin=0.0, rmax=1.0):
    return (rmax-rmin)*random() + rmin

class Particle:
    def __init__(self, x, y, trace = True):
        self.trace = trace
        if trace:
            self.x = [x]
            self.y = [y]
            self.line = plt.plot(self.x, self.y, '-')[0]
            self.particle = plt.plot(x, y, 'o')[0]
        else:
            self.x = x
            self.y = y
            self.particle = plt.plot(x, y, 'o')[0]
    def move(self, x, y):
        if self.trace:
            self.x.append(x)
            self.y.append(y)
            self.line.set_data(self.x, self.y)
            self.particle.set_data(x, y)
        else:
            self.x = x
            self.y = y
            self.particle.set_data(x, y)
    def clear(self):
        if self.trace:
            self.x = []
            self.y = []
            self.line.set_data([], [])
            self.particle.set_data([], [])
        else:
            self.x = 0
            self.y = 0
            self.particle.set_data([], [])

class Canvas:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        plt.axis([xmin,xmax,ymin,ymax])
        plt.axis('square')
        plt.grid()
        self.update()
    def show(self):
        plt.show()
    def update(self, t = None):
        plt.pause(0.01)
        if t:
            plt.title( str(t) )

canvas = Canvas(-10, 10, -10, 10)
a = Particle(0, 0)
b = Particle(-10, -10) 
c = Particle(0, 0, False) 
d = Particle(0, 0, False) 
e = Particle(0, 0, False) 

t = 0
tmax = 100
dt = 0.1
while (t <= tmax):
    a.move( t/10*np.cos(t), t/10*np.sin(t) )
    b.move( t/5-10, t/5-10 )
    c.move( rand(-10, 10), rand(-10, 10) )
    d.move( rand(-10, 10), rand(-10, 10) )
    e.move( rand(-10, 10), rand(-10, 10) )
    canvas.update(t)
    t += dt

canvas.show()