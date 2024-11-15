import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Canvas:
    def __init__(self, xmin, ymin, xmax, ymax):
        fig = plt.figure(figsize=(18, 18))
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        plt.axis([xmin,xmax,ymin,ymax])
        plt.axis('scaled')
        plt.grid()
        plt.tight_layout()
        self.update()
    def show(self):
        plt.show()
    def update(self, t = None):
        plt.pause(0.01)
        if t:
            plt.title( f'{round(t)}s' )
    def rectangle(self,x,y,w,h,color,alpha=0.2):
        r = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
        ax = plt.gca()
        ax.add_patch(r)
        return r
    def circle(self,x,y,r=5,color='black',alpha=0.5):
        c = patches.Circle((x, y), r, linewidth=1, edgecolor=color, facecolor=color, alpha=alpha)
        ax = plt.gca()
        ax.add_patch(c)
        return c
    def parabola(self,x,y,color='red',alpha=0.5):
        A = np.array([[x[0]**2, x[0], 1],
                      [x[1]**2, x[1], 1],
                      [x[2]**2, x[2], 1]])
        b = np.array(y)
        coefficients = np.linalg.solve(A, b)
        a, b, c = coefficients
        u = np.linspace(min(x) - 1, max(x) + 1, 500)
        v = a * u**2 + b * u + c
        plt.plot(u,v,color=color,alpha=alpha)
        return x,y,a,b,c
