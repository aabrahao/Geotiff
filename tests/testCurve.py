import numpy as np
import matplotlib.pyplot as plt

def generate_figure_eight_trajectory(point, scale, num_points=500):
    # Define the crossing point (center of the figure-eight path)
    x0, y0 = point
    
    # Generate a figure-eight (lemniscate) curve with parameter t
    t = np.linspace(0, 2 * np.pi, num_points)
    x = x0 + scale * np.sin(t)
    y = y0 + scale * np.sin(t) * np.cos(t)
    
    # Plot the trajectory path
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Figure-Eight Path", linewidth=2)
    plt.plot(x0, y0, 'ro', label="Crossing Point")  # Mark the crossing point
    
    # Set plot details
    plt.title("Robot Trajectory with Double Normal Crossing")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example parameters
crossing_point = (0, 0)  # The point where the robot should cross twice perpendicularly
scale = 5                # Scale of the figure-eight (size of the loops)

generate_figure_eight_trajectory(crossing_point, scale)