# 3D Rotation Experiments

A small computer-graphics project created at MISIS in 2022 to explore 3D
transformations without a game engine.

## What was implemented

- `CubeRotate.py` defines cube vertices, applies rotation and orthographic
  projection matrices with NumPy, and renders the wireframe using Pygame.
- `OpenGl.py` is a separate OpenGL exercise that renders a lit, rotatable tree
  assembled from a cylinder and cones. The arrow keys change its rotation.

## Technologies

- Python
- NumPy
- Pygame
- PyOpenGL and GLUT

## Running the project

For the cube experiment:

```bash
pip install numpy pygame
python CubeRotate.py
```

For the OpenGL tree experiment:

```bash
pip install PyOpenGL PyOpenGL-accelerate
python OpenGl.py
```

The OpenGL example also requires a system installation of GLUT or FreeGLUT.

## Known limitations

- The cube uses fixed rotation matrices and does not currently expose
  interactive controls.
- The Pygame window is not explicitly cleared between frames.
- The two files are independent experiments rather than one application.
- Comments in the OpenGL exercise remain in Russian.

## Historical note

The project was written by hand before generative AI coding assistants became
widely available. It is preserved as an early graphics and linear-algebra
exercise.
