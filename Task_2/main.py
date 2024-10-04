import numpy as np
import matplotlib.pyplot as plt
from skeleton_visualizer import Rotation, Link, Visualizer3D, get_input

# User inputs for angles and length, with default values for easier testing
L0 = 180  # mm
L1 = 335  # mm
L2 = 355  # mm

# Use default values if needed for debugging
theta_0 = np.radians(get_input("Enter θ₀ (angle between X and OAB plane): ", 30))  # Default: 30 degrees
theta_1 = np.radians(get_input("Enter θ₁ (angle between OA and AB): ", 45))  # Default: 45 degrees
theta_2 = np.radians(get_input("Enter θ₂ (angle ∠ABC): ", 60))  # Default: 60 degrees

# Base points
O = np.array([0, 0, 0])
A_star = np.array([0, 0, L0])
B_star = np.array([0, L1 * np.cos(theta_1), L1 * np.sin(theta_1)])

# Apply rotation for point A and B
R = Rotation.rotation_matrix_z(theta_0)
A = R @ A_star
B = R @ B_star

# Create Link BC
link_BC = Link('BC', B, theta_2, L2)
C = link_BC.get_transformed_point(B)

# Visualize with animation
visualizer = Visualizer3D()
points_sequence = [
    [O, A, B, C],  # Start configuration
    [O, A, B, link_BC.get_transformed_point(B)]  # Updated configuration for animation
]

connections = [(O, A), (A, B), (B, C)]
visualizer.animate(points_sequence, connections, interval=500)

# Keep the plot open
plt.show()
