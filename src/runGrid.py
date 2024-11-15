import numpy as np
import matplotlib.pyplot as plt
from random import random 
from Canvas import Canvas
from Particle import Particle
from Robot import Robot

def rand(rmin=0.0, rmax=1.0):
    return (rmax-rmin)*random() + rmin

def inside(xc,yc,x,y,r):
    if abs(xc - x) <= r and abs(yc - y) <= r:
        print('Inside!')
        return True
    else:
        return False

def resampleRose(a,k,n,xc,yc,robot,canvas):
    print('Resampling rose...')
    theta = 0
    dtheta = 2*np.pi/n
    while (True): 
        r = a*np.cos(k * theta)
        x = xc + r * np.cos(theta)
        y = yc + r * np.sin(theta)
        theta = theta + dtheta
        if theta >= np.pi:
             break
        robot.move( x, y )
        canvas.update()
    return x,y

def nomalParabola(x,y,a,b,c):
    slope = 2 * a * x + b
    n = (-(2 * a * x + b), 1)
    l = np.sqrt(n[0]**2 + n[1]**2)
    n = (n[0] / l, n[1] / l)
    return n[0],n[1]

def resampleParabola(px,py,a,b,c,x,y,n,d,particle,canvas):
        print('Resampling parabola...')
        u = np.linspace(min(px) - 1, max(px) + 1, n)
        v = a * u**2 + b * u + c
        # Normals
        nu = 0*u
        nv = 0*v
        for i in range(len(u)):
            nu[i], nv[i] = nomalParabola(u[i],v[i],a,b,c)
        # Upper
        uu = u + d*nu
        vu = v + d*nv
        # Lower
        ul = u - d*nu
        vl = v - d*nv
        # Reorder
        uu = np.flip(uu)
        vu = np.flip(vu)
        ul = np.flip(ul)
        vl = np.flip(vl)
        #plt.plot(uu,vu,'^')
        #plt.plot(ul,vl,'o')
        n = len(uu)
        i = 0
        plt.pause(.1)
        while i < n:
            particle.move(ul[i],vl[i])
            plt.pause(.1)
            particle.move(uu[i],vu[i])
            plt.pause(.1)
            particle.move(uu[i+1],vu[i+1])
            plt.pause(.1)
            particle.move(ul[i+1],vl[i+1])
            plt.pause(.1)
            i = i + 2
        return x,y

def main():
    b = 0.1
    dy = 30 # ft
    v = 3 # ft/s
    x = 0
    y = 15
   
    xmin = 0.0
    ymin = 0.0
    xmax = 5*dy
    ymax = 3*dy
    lx = xmax - xmin
    ly = ymax - ymin
    b = b*lx

    canvas = Canvas(xmin, ymin, xmax, ymax)

    canvas.rectangle(xmin, ymin, lx, dy,'red',0.1)
    canvas.rectangle(xmin, ymin+2*dy, lx, dy,'red',0.1)

    #canvas.circle(70,55,.2)
    #canvas.circle(50,50,.2)
    #canvas.circle(40,35,.2)
    
    #erosion = Particle(70,xmin + 1.5*dy,'white',False)
    px,py,pa,pb,pc = canvas.parabola([70,50,40],[55,50,35],'black')
    scannedParabola = False

    robot = Robot(x, y)
    defect = Particle(xmin + 0.5*lx, ymin + 0.5*dy, 'black', False)
    scannedDefect = False

    t = 0
    tmax = 100
    dt = 0.001
    while (t <= tmax):
        if ( y > ymax - 0.5*dy):
            break
        elif defect.inside(x,y,.5) and scannedDefect == False:
            x,y = resampleRose(12,3,1000,x,y,robot.particle,canvas)
            scannedDefect = True
        elif inside(70,xmin + 1.5*dy,x,y,.5) and scannedParabola == False:
            x,y = resampleParabola(px,py,pa,pb,pc,x,y,50,4,robot.particle,canvas)
            scannedParabola = True
        elif ( v > 0 and x >= xmax - b):
            y = y + dy
            v = -v
        elif ( v < 0 and x <= xmin + b):
            y = y + dy
            v = -v
        else:
            x = x + v*t
        robot.move(x, y, v)
        canvas.update(t)
        t += dt

    print('Done!')
    canvas.show()
    
if __name__ == "__main__":
    main() 


