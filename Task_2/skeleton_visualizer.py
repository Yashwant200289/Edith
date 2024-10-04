import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Rotation:
    @staticmethod
    def rotation_matrix_z(theta):
        """Returns the rotation matrix for a rotation around the Z-axis by theta radians."""
        return np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])

class Link:
    def __init__(self, identifier, prev_point, angle, length):
        self.identifier = identifier
        self.prev_point = prev_point
        self.angle = angle
        self.length = length

    def get_transformed_point(self, prev_point):
        """Calculates the new point based on the previous point and the current angle and length."""
        return prev_point + np.array([self.length * np.cos(self.angle), self.length * np.sin(self.angle), 0])

class Visualizer3D:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def visualize(self, points, connections):
        """Visualizes points and connections in 3D space."""
        for idx, point in enumerate(points):
            self.ax.scatter(*point, label=f'Point {idx} ({point[0]}, {point[1]}, {point[2]})')

        for connection in connections:
            p1, p2 = connection
            self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]])

        self.ax.legend()
        plt.draw()

    def animate(self, points_sequence, connections, interval=100):
        """Animates the motion of points in 3D space."""
        for points in points_sequence:
            self.ax.cla()  # Clear previous points
            self.visualize(points, connections)
            plt.pause(interval / 1000)  # Pause for animation effect

def get_input(prompt, default=None):
    """Helper function to get user input and handle errors."""
    try:
        return float(input(prompt))
    except ValueError:
        if default is not None:
            print(f"Invalid input. Using default value: {default}")
            return default
        else:
            raise ValueError("Invalid input and no default value provided.")
