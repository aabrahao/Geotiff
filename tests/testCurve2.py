import numpy as np
import matplotlib.pyplot as plt

def generate_rotated_figure_eight(crossing_point, scale, rotation_angle, num_points=500):
    # Define the crossing point
    x_center, y_center = crossing_point

    # Generate a figure-eight (lemniscate) curve with parameter t
    t = np.linspace(0, 2 * np.pi, num_points)
    x = scale * np.sin(t)
    y = scale * np.sin(t) * np.cos(t)

    # Rotate the figure-eight by the specified angle
    rotation_matrix = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle)],
        [np.sin(rotation_angle), np.cos(rotation_angle)]
    ])
    rotated_points = np.dot(rotation_matrix, np.array([x, y]))
    x_rotated = rotated_points[0] + x_center
    y_rotated = rotated_points[1] + y_center

    # Plot the trajectory path
    plt.figure(figsize=(8, 6))
    plt.plot(x_rotated, y_rotated, label="Rotated Figure-Eight Path", linewidth=2)
    plt.axline(crossing_point, slope=np.tan(rotation_angle), color='gray', linestyle='--', label="Rotated Horizontal Line")
    plt.scatter([x_center], [y_center], color='red', label="Crossing Point", zorder=5)  # Mark crossing point
    
    # Set plot details
    plt.title("Rotated Robot Trajectory with Crossing")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example parameters
crossing_point = (0, 0)        # The crossing point of the path
scale = 5                      # Scale of the figure-eight
rotation_angle = np.pi / 4     # Rotate the path by 45 degrees (π/4 radians)

generate_rotated_figure_eight(crossing_point, scale, rotation_angle)