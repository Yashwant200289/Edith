# Skeletal Visualization in 3D

## Overview

This project visualizes a skeletal system in 3D with multiple links (O-A, A-B, B-C). The positions of the points are controlled by user inputs for the angles between the links. Additionally, it allows adding another link (BC) and transforming points in the 3D space according to user-specified angles.

## Problem 1: Visualizing Points O, A, and B

### Description:
- Points O, A, and B represent a skeletal structure in 3D.
- The angles `θ₀` (rotation around the Z-axis) and `θ₁` (angle between OA and AB) are taken as user inputs.
- The script visualizes these points and draws lines between them to represent the links OA and AB.

### User Inputs:
- `θ₀`: The rotation angle of the OAB plane around the Z-axis.
- `θ₁`: The angle between the links OA and AB.

### Output:
- A 3D plot showing the points O, A, and B, and the links connecting them.
  
## Problem 2: Adding Link BC

### Description:
- An additional link, BC, is added to the skeleton, where `BC` is coplanar with OAB.
- The angle `θ₂` (angle between AB and BC) and the distance between B and C (fixed at 355 mm) are used to compute the position of point C.
- This link is visualized along with OA and AB in 3D space.

### User Inputs:
- `θ₂`: The angle between links AB and BC.

### Output:
- A 3D plot showing points O, A, B, and C, with the links OA, AB, and BC.

## Setup and Installation

### Prerequisites:
- Python 3.x
- Libraries: `numpy`, `matplotlib`

To install the required libraries, run:
```bash
pip install numpy matplotlib
