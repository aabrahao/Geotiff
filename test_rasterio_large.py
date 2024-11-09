import rasterio as rio
import rasterio.plot as rioplt
import rasterio.windows as riownd
import numpy as np
import matplotlib.pyplot as plt

def length(dataset):
    lx = dataset.bounds.right - dataset.bounds.left
    ly = dataset.bounds.top - dataset.bounds.bottom
    return lx, ly

def resolution(dataset):
    lx, ly = length(dataset)
    dx = lx/dataset.width
    dy = ly/dataset.height
    return dx, dy

def info(dataset):
    print('File:', dataset.name)
    print('Driver:', dataset.driver)
    print('Mode:', dataset.mode)
    print('Size:', dataset.width, 'x', dataset.height)
    print('Bands:', dataset.count)
    print('Coordnates:', dataset.crs)
    print('Bounds:', dataset.bounds)
    print('Transform:', dataset.transform)
    lx, ly = length(dataset)
    dx, dy = resolution(dataset)
    print('Resolution:',dx,'x',dy )
    print('Dimension:',lx,'x',ly)

def open(filename):
    with rio.open(filename) as dataset:
        pass
    info(dataset)
    return dataset

def grid(dataset, band=1):
    xr = np.linspace( dataset.bounds.left, dataset.bounds.right, dataset.width)
    yr = np.linspace( dataset.bounds.top, dataset.bounds.bottom, dataset.height)
    x, y = np.meshgrid(xr, yr) 
    z = dataset.read(band)
    return x, y, z

def plot(x,y,z):
    plt.figure()
    plt.imshow(z, cmap = 'jet')
    plt.show(block=False)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d', proj_type = 'ortho')
    ax.plot_surface(x, y, z, cmap='jet',linewidth=0, antialiased=False)
    ax.set_position([0, 0, 1, 1])
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.view_init(90, -90, 0)
    ax.set_aspect('equal')

    plt.grid()
    plt.show()

def showt():
    plt.show(block=False)


def main(): 
    dataset = open('data/gadas.tif')
    dataset = open('rifle.tif')
    info(dataset)
    print(dataset.xy(0,0))
    print(dataset.xy(dataset.width, dataset.height))
    #x,y,z = grid(dataset)
    #plot(x,y,z)

if __name__ == "__main__":
    main()