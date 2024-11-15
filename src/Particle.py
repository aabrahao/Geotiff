import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, x, y, color = 'red', trace = True):
        self.trace = trace
        if trace:
            self.x = [x]
            self.y = [y]
            self.line = plt.plot(self.x, self.y, '-', alpha = .5, color = color)[0]
            self.particle = plt.plot(x, y, 'o', alpha = .5, color = color)[0]
        else:
            self.x = x
            self.y = y
            self.particle = plt.plot(x, y, 'o', color = color)[0]
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
    def inside(self,x,y,r):
        if abs(self.x - x) <= r and abs(self.y - y) <= r:
            print('Inside!')
            return True
        else:
            return False
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
