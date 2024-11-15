#!/usr/bin/env python

# My Oscilloscope
# FIU-ARC
# Summer 2024

import numpy as np
import matplotlib.pyplot as plt

# Limits
xmin = 0
xmax = 3*np.pi
ymin = -3.5
ymax = 3.5  

# Signals
x = np.linspace(xmin,xmax, 100)
y1 = 2*np.sin(x)
y2 = 3*np.cos(x)

# Initialize
plt.axis([xmin,xmax,ymin,ymax])
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('My Oscilloscope')
plt.grid()
plt.pause(0.2) # Draw now!

# Plot signals
l1 = plt.plot(x,y1,'-')[0]
l2 = plt.plot(x[0],y1[0],'o')[0]
l3 = plt.plot(x[0],y2[0],'-')[0]
l4 = plt.plot(x[0],y2[0],'s')[0]
plt.pause(0.2)

# Update signals
for i in range(len(x)):
    l2.set_data(x[i],y1[i])
    l3.set_data(x[0:i],y2[0:i])
    l4.set_data(x[i],y2[i])
    plt.pause(0.2)

plt.show()
