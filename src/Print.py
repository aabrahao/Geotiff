import numpy as np
from pprint import pprint

def disp(*args):
    if len(args) == 0:
        print('')
    else:
        for arg in args:
            print(arg, end='')

def section(title=None):
    print('-------------------')
    if title is not None:
        print(title)

def field(name, *args):
    disp(f'{name}: ')
    n = len(args)
    for i in range(0, n):
        arg = args[i]
        if type(arg) is str:
            disp(f"'{arg}'")
        else:
            disp(arg)
        if i < n-1:
            disp(',')
    disp()

def json(data):
    pprint(data)

def array(x):
    field('Shape', x.shape)
    field('Type', x.dtype)
    if x.size != 0:
        field('Range', (np.nanmin(x), np.nanmax(x)))
        field('Meadian', np.nanmedian(x))
        field('Mean', np.nanmean(x))
        field('Std', np.nanstd(x))

# Actual and observed
def error(a, o): 
    field(f'Error |{a}-{o}|', np.abs(o - a))
