import numpy as np
import matplotlib.pyplot as plt
from random import random 
import Canvas as cv
from scipy.integrate import quad

def main():
    canvas = cv.Canvas(-10, -10, 10, 10)
    robot = cv.Particle(0, 0)

    a = 5
    k = 3
    v = 3
    T = time_to_draw_rose(a, k, v) 

    theta = 0
    t = 0
    tmax = T
    dt = 0.01
    while (t <= tmax):
        r = a*np.cos(k*theta)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        dr_dtheta = a * k * np.cos(k * theta)
        ds_dtheta = np.sqrt(dr_dtheta**2 + r**2)
        dtheta = v * dt / ds_dtheta
        theta += dtheta
        t += dt
        robot.move( x, y )
        canvas.update(t)
        
    canvas.show()
    
if __name__ == "__main__":
    main() 

    xc = 0.0
    xc = 0.0
    angle = np.pi / 4
    scale = 5
    
    t = np.linspace(0, 2 * np.pi, num_points)
    x = scale * np.sin(t)
    y = scale * np.sin(t) * np.cos(t)

    
    rotation = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    rotated_points = np.dot(rotation_matrix, np.array([x, y]))
    x_rotated = rotated_points[0] + xc
    y_rotated = rotated_points[1] + yc

    