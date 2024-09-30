import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Function to apply rotation matrix
def rotation_matrix_z(theta):
    """Returns the rotation matrix for a rotation around the Z-axis by theta radians."""
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


# Function to visualize the points in 3D
def visualize_3D(O, A, B, C=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot points O, A, B
    ax.scatter(*O, color='r', label='O (0, 0, 0)')
    ax.scatter(*A, color='g', label=f'A ({A[0]}, {A[1]}, {A[2]})')
    ax.scatter(*B, color='b', label=f'B ({B[0]}, {B[1]}, {B[2]})')

    # Plot lines OA and AB
    ax.plot([O[0], A[0]], [O[1], A[1]], [O[2], A[2]], color='g')
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='b')

    if C is not None:
        ax.scatter(*C, color='purple', label=f'C ({C[0]}, {C[1]}, {C[2]})')
        ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='purple')

    ax.legend()
    plt.show()


# Problem 1: User inputs for angles and length
L0 = 180  # mm
L1 = 335  # mm
theta_0 = np.radians(float(input("Enter θ₀ (angle between X and OAB plane): ")))  # Convert to radians
theta_1 = np.radians(float(input("Enter θ₁ (angle between OA and AB): ")))

# Base points
O = np.array([0, 0, 0])
A_star = np.array([0, 0, L0])
B_star = np.array([0, L1 * np.cos(theta_1), L1 * np.sin(theta_1)])

# Apply rotation
R = rotation_matrix_z(theta_0)
A = R @ A_star
B = R @ B_star

# Visualize the result
visualize_3D(O, A, B)


# Problem 2: Adding link BC with length 355 mm and angle θ₂
class Link:
    def __init__(self, identifier, prev_link, angle, length, motion_limits=(0, np.pi), acceleration=0, max_velocity=0):
        self.identifier = identifier
        self.prev_link = prev_link
        self.angle = angle
        self.length = length
        self.motion_limits = motion_limits
        self.acceleration = acceleration
        self.max_velocity = max_velocity

    def get_transformed_point(self, prev_point):
        # Calculate the new point based on the previous point and the angle
        return prev_point + np.array([self.length * np.cos(self.angle), self.length * np.sin(self.angle), 0])


# User input for θ₂
theta_2 = np.radians(float(input("Enter θ₂ (angle ∠ABC): ")))
link_BC = Link('BC', 'AB', theta_2, 355)

# Compute point C
C = link_BC.get_transformed_point(B)

# Visualize the extended skeleton with BC
visualize_3D(O, A, B, C)
