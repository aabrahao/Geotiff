import numpy as np
import matplotlib.pyplot as plt
from random import random 
import Canvas as cv
from scipy.integrate import quad

def rand(rmin=0.0, rmax=1.0):
    return (rmax-rmin)*random() + rmin

def main():
    canvas = cv.Canvas(-10, -10, 10, 10)
    robot = cv.Particle(0, 0)

    a = 5
    k = 3
    n = 2000

    theta = 0
    dtheta = 2*np.pi/n

    while (True): 
        r = a*np.cos(k * theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        theta = theta + dtheta
        if theta >= np.pi:
             break
        robot.move( x, y )
        canvas.update()
        
    canvas.show()
    
if __name__ == "__main__":
    main() 


