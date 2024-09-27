import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Function to create a rotation matrix around the Z-axis
def rotation_matrix_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


# Function to visualize the points O, A, B in 3D
def visualize_OAB(L0, L1, theta0, theta1):
    # Original points A* and B* before rotation
    O = np.array([0, 0, 0])
    A_star = np.array([0, 0, L0])
    B_star = np.array([0, L1 * np.cos(theta1), L1 * np.sin(theta1)])

    # Apply the rotation matrix to A* and B*
    R = rotation_matrix_z(theta0)
    A = R.dot(A_star)
    B = R.dot(B_star)

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot points
    ax.scatter(*O, color='r', label='O (origin)')
    ax.scatter(*A, color='g', label='A (after rotation)')
    ax.scatter(*B, color='b', label='B (after rotation)')

    # Plot lines
    ax.plot([O[0], A[0]], [O[1], A[1]], [O[2], A[2]], color='g')
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='b')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot limits
    ax.set_xlim([-500, 500])
    ax.set_ylim([-500, 500])
    ax.set_zlim([0, 500])

    ax.legend()
    plt.show()


# Take user inputs for θ0 and θ1
theta0 = float(input("Enter θ₀ (rotation around Z-axis in radians): "))
theta1 = float(input("Enter θ₁ (angle between OA and AB in radians): "))

# Length of the links (in mm)
L0 = 180
L1 = 335

# Visualize O, A, B in 3D space
visualize_OAB(L0, L1, theta0, theta1)
