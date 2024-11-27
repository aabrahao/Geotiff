import numpy as np

def toRadian(rad):
    return np.deg2rad(rad)

def toDegree(deg):
    return np.rad2deg(deg)

def array(n=None):
    if n is None:
        x = np.array([], dtype=np.float64)
    elif isinstance(n, int):
        x = np.empty(n, dtype=np.float64)
    elif isinstance(n, list):
        x = np.array(n, dtype=np.float64)
    else:
        print('Ops, vector type not implemented, empty vector returned!')
        x = np.array([], dtype=np.float64)
    return x

def vector(n=None):
    x = array(n)
    y = np.copy(x)
    return x, y

def toVector(x, y): # List to vector
    return np.array(x), np.array(y)

def direction(angle):
    return np.cos(angle), np.sin(angle)

def size(x):
    return x.size

def isempty(x):
    if size(x) == 0:
        return True
    else:
        return False

def disp(x):
    print(x)

def length(x, y):
    return np.sqrt( x*x + y*y )

def unit(x, y):
    d = length(x,y)
    return x/d, y/d

def normal(x,y):
    return -y, x

def dot(x1,y1,x2,y2):
    return x1*x2 + y1*y2

# o: Origin point
# v: Direction vector
# x,y: Points to project
def project(ox, oy, vx, vy, x, y):
    ux, uy = unit(vx, vy)
    d = dot(ux, uy, x-ox, y-oy)
    return ox + d*ux, oy + d*uy

def append(x,y,xa,ya):
    return np.append(x, xa), np.append(y, ya)