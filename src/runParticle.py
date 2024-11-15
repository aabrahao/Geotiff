import numpy as np
import matplotlib.pyplot as plt
from random import random 
import Canvas as cv

def rand(rmin=0.0, rmax=1.0):
    return (rmax-rmin)*random() + rmin

def main():
    canvas = cv.Canvas(-10, -10, 10, 10)
    a = cv.Particle(0, 0)
    b = cv.Particle(-10, -10) 
    c = cv.Particle(0, 0, False) 
    d = cv.Particle(0, 0, False) 
    e = cv.Particle(0, 0, False) 

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
    
if __name__ == "__main__":
    main() 


