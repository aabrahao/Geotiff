import numpy as np

x = np.array([(122.0, 1.0, -47.0), (123.0, 1.0, -47.0), (125.0, 1.0, -44.0)])

print(x)

x[x==1.0] = np.nan

print(x)