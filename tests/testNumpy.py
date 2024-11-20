import numpy as np

def toPoints(x,y):
    points = list(zip(x,y))
    return points

def toNumpy(points):
    xy = np.array(points)
    return xy[:,0], xy[:,1]

print('#######################################################')
print('Test Mask')
x = np.array([(122.0, 1.0, -47.0), (123.0, 1.0, -47.0), (125.0, 1.0, -44.0)])
print(x)
x[x==1.0] = np.nan
print(x)

print('#######################################################')
print('Test points')

points = [(1,2),(3,4),(5,6)]
print(points)
print(len(points))

xy = np.array(points)
print(xy)
print(xy.shape)

x,y = toNumpy(points)
print(x)
print(x.shape)
print(y)
print(y.shape)

points = toPoints(x,y)
print(points)
print(len(points))

