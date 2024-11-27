import numpy as np
from numpy import pi
import Cad as cad
import Vector as vc

def main():
    x, y = vc.vector(5)
    z = vc.array([1,2,3,4,5])
    w = vc.array()
   
    print(x)
    print(y)
    print(z)
    print(w)

    print(vc.size(x))

    a = np.linspace(0, 2*pi, vc.size(x))
    x = 10*np.cos(a)
    y = 10*np.sin(a)

    print(x)
    print(y)

    print(z * z)
    print(vc.length(x,y))

    u, v = vc.unit(1,1)

    print(u)
    print(v)
    print(vc.length(u,v))

    print(vc.dot(x,y,u,v))
    print(vc.dot(0.5,0.5,u,v))

if __name__ == "__main__":
    main() 
